def solve():
    n = int(input())
    s, t = map(list,input().split())
    ans = ''
    for i in range(n):
        ans += s[i]
        ans += t[i]
    print(ans)



if __name__ == '__main__':
    solve()
