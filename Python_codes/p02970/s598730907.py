def solve():
    N, D = map(int, input().split())
    left = 1+2*D
    ans = 1
    while left < N:
        left = left + 1 + 2*D
        ans += 1
    print(ans)


solve()
