def main():
    N, M, Q = map(int, input().split())
    t = [[0] * N for _ in range(N)]
    for _ in range(M):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        t[l][r] += 1
    s = [[0] * N for _ in range(N)]
    s[0][0] = t[0][0]
    for i in range(1, N):
        s[0][i] = s[0][i-1] + t[0][i]
    for i in range(1, N):
        s[i][0] = s[i-1][0] + t[i][0]
    for i in range(1, N):
        for j in range(1, N):
            s[i][j] = s[i-1][j] + s[i][j-1] + t[i][j] - s[i-1][j-1]
    for _ in range(Q):
        p, q = map(int, input().split())
        if p == 1:
            print(s[q-1][q-1])
            continue
        p -= 1
        q -= 1
        print(s[q][q] - s[q][p-1] - s[p-1][q] + s[p-1][p-1])
main()
