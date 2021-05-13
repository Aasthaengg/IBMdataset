def resolve():
    import sys
    input = sys.stdin.readline
    # 整数 1 つ
    # n = int(input())
    # 整数複数個
    n, ma, mb = map(int, input().split())
    # 整数 N 個 (改行区切り)
    # N = [int(input()) for i in range(N)]
    # 整数 N 個 (スペース区切り)
    # N = list(map(int, input().split()))
    # 整数 (縦 H 横 W の行列)
    A = [list(map(int, input().split())) for i in range(n)]

    Cost = [[[5000] * 401 for _ in range(401)] for _ in range(n+1)]
    Cost[0][0][0] = 0

    for i in range(n):
        for j in range(400):
            for k in range(400):
                if j+A[i][0] <= 400 and k+A[i][1] <= 400:
                    Cost[i+1][j+A[i][0]][k+A[i][1]] = min(Cost[i+1][j+A[i][0]][k+A[i][1]], Cost[i][j][k]+A[i][2])
                Cost[i+1][j][k] = min(Cost[i+1][j][k], Cost[i][j][k])

    costmin = 5000
    for a in range(1,401):
        for b in range(1,401):
            if a * mb == b * ma:
                costmin = min(costmin, Cost[n][a][b])
    if costmin == 5000:
        print(-1)
    else:
        print(costmin)


resolve()