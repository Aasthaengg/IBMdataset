def resolve():
    # 整数 1 つ
    n = int(input())
    # 整数複数個
    # a, b, c = list(map(int, input().split()))
    # 整数 N 個 (改行区切り)
    # N = [int(input()) for i in range(N)]
    # 整数 N 個 (スペース区切り)
    # N = list(map(int, input().split()))
    # 整数 (縦 H 横 W の行列)
    # A = [list(map(int, input().split())) for i in range(H)]

    re = 1000
    for a in range(1, (n//2)+1):
        b = n - a
        sumnum = 0
        while a >= 1:
            sumnum += a % 10
            a = a //10
        while b >= 1:
            sumnum += b % 10
            b = b //10
        if re > sumnum:
            re = sumnum

    print(re)
resolve()