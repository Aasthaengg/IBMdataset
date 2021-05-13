def solve():
    N, M = map(int, input().split())
    Count = [0] * (N + 1)
    for i in range(M):
        l, r = map(int, input().split())
        Count[l-1] += 1
        Count[r] -= 1
    ans = 0
    if Count[0] == M: ans = 1
    for i in range(1, N):
        Count[i] += Count[i-1]
        if Count[i] == M: ans += 1
    print(ans)


if __name__ == "__main__":
    solve()