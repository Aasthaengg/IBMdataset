def solve():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    ans = 0
    for i in range(n)[::-1]:
        if (a[i]+ans)%b[i]:
            ans+=b[i]-(a[i]+ans)%b[i]
    print(ans)
if __name__=='__main__':
    solve()