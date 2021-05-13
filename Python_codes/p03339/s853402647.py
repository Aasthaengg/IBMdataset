def resolve():
    # 整数 1 つ
    n = int(input())
    s = input()
    # 整数複数個
    # a, b = map(int, input().split())
    # 整数 N 個 (改行区切り)
    # N = [int(input()) for i in range(N)]
    # 整数 N 個 (スペース区切り)
    # N = list(map(int, input().split()))
    # 整数 (縦 H 横 W の行列)
    # A = [list(map(int, input().split())) for i in range(H)]

    cntW = 0
    for i in range(1, n):
        if s[i] == "W":
            cntW += 1

    cntmax = cntW
    for i in range(1, n):
        if s[i-1] == "E":
            cntW += 1
        if s[i] == "W":
            cntW -= 1
        if cntmax < cntW:
            cntmax = cntW

    print(n - cntmax -1)


resolve()