def resolve():
    import sys
    input = sys.stdin.readline
    # 整数 1 つ
    # n = int(input())
    # 整数複数個
    a, b, k = map(int, input().split())
    # 整数 N 個 (改行区切り)
    # N = [int(input()) for i in range(N)]
    # 整数 N 個 (スペース区切り)
    # N = list(map(int, input().split()))
    # 整数 (縦 H 横 W の行列)
    # A = [list(map(int, input().split())) for i in range(H)]

    List = [x for x in range(1, min(a,b)+1)]
    List.sort(reverse=True)

    cnt = 0
    for y in List:
        if a % y == 0 and b % y == 0:
            cnt += 1
            if cnt == k:
                print(y)
                break
resolve()