def main():
    MOD = 10 ** 9 + 7
    N, M = map(int, input().split())
    S = tuple(map(int, input().split()))
    T = tuple(map(int, input().split()))
    l = [[0] * (M + 1) for _ in range(N + 1)]
    l[0] = [1] * (M + 1)
    for i in range(N + 1):
        l[i][0] = 1
    r = 1
    for i in range(1, N+1):
        for j in range(1, M+1):
            if S[i-1] == T[j-1]:
                r += l[i-1][j-1]
                l[i][j] = l[i][j-1] + l[i-1][j]
                l[i][j] %= MOD
            else:
                l[i][j] = l[i][j-1] + l[i-1][j] - l[i-1][j-1]
        r %= MOD
    print(r % MOD)
main()
