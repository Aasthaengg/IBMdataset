def solve():
    N, X = map(int, input().split())
    m = [int(input()) for _ in range(N)]
    ans = N
    X = X - sum(m)
    ans += X // min(m)
    print(ans)





if __name__ == "__main__":
    solve()