def solve():
    n = int(input())
    x, l = [0]*n, [0]*n
    for i in range(n):
        x[i], l[i] = map(int, input().split())
    hoge = []
    for i in range(n):
        hoge.append([x[i]+l[i], x[i]-l[i]])
    hoge.sort()
    t = -1000000000000000000000
    ans = 0
    for i in range(n):
        if t <= hoge[i][1]:
            ans += 1
            t = hoge[i][0]
    print(ans)
    return 0
 
if __name__ == "__main__":
    solve()