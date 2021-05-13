def resolve():
    # 整数 1 つ
    n = int(input())
    # 整数複数個
    # a, b = map(int, input().split())
    # 整数 N 個 (改行区切り)
    # N = [int(input()) for i in range(N)]
    # 整数 N 個 (スペース区切り)
    A = list(map(int, input().split()))
    # 整数 (縦 H 横 W の行列)
    # A = [list(map(int, input().split())) for i in range(H)]

    cnt = 0
    for x in A:
        if x % 2 == 1:
            cnt += 1

    if cnt % 2 == 0:
        print("YES")
    else:
        print("NO")


resolve()