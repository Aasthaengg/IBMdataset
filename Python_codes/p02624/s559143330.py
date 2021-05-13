def solve():
    N = int(input())
    ans = 0
    for k in range(1, N+1):
        x = N // k
        ans += x * (k + x*k) // 2
    print(ans)

if __name__ == "__main__":
    solve()