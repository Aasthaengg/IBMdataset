def resolve():
    # 整数 1 つ
    # n = int(input())
    # 整数複数個
    n, k = map(int, input().split())
    # 整数 N 個 (改行区切り)
    # N = [int(input()) for i in range(N)]
    # 整数 N 個 (スペース区切り)
    A = list(map(int, input().split()))
    # 整数 (縦 H 横 W の行列)
    # A = [list(map(int, input().split())) for i in range(H)]

    Dic = {x:0 for x in set(A)}
    if len(Dic) <= k:
        print(0)
    else:
        for y in A:
            Dic[y] += 1
        DIcsort = sorted(Dic.items(), key=lambda x: x[1])

        cnt = 0
        for i in range(len(Dic) - k):
            cnt += DIcsort[i][1]

        print(cnt)
resolve()