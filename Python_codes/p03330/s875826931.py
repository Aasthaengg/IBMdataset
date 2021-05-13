def main():
    N, C = map(int, input().split())
    D = []
    for _ in range(C):
        d = list(map(int, input().split()))
        D.append(d)
    c = []
    for _ in range(N):
        cc = list(map(int, input().split()))
        c.append(cc)
    l = [[0] * (C+1) for _ in range(3)]
    for i in range(N):
        for j in range(N):
            l[(i + j) % 3][c[i][j]] += 1
    m = pow(10, 10000)
    for i in range(1, C+1):
        for j in range(1, C+1):
            for k in range(1, C+1):
                if i == j or i == k or j == k:
                    continue
                t = 0
                for ii in range(1, C+1):
                    t += l[0][ii] * D[ii-1][i-1]
                for jj in range(1, C+1):
                    t += l[1][jj] * D[jj-1][j-1]
                for kk in range(1, C+1):
                    t += l[2][kk] * D[kk-1][k-1]
                m = min(m, t)
    print(m)
main()
