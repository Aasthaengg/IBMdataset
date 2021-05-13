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

#偶数項を正とする
    sumeven = 0
    cnteven = 0
    for i in range(n):
        sumeven += A[i]
        if i % 2 == 0:
            if sumeven <= 0:
                cnteven += abs(sumeven) + 1
                sumeven += abs(sumeven) + 1
        else:
            if sumeven >= 0:
                cnteven += (sumeven + 1)
                sumeven -= (sumeven + 1)

# 奇数項を正とする
    sumodd = 0
    cntodd = 0
    for i in range(n):
        sumodd += A[i]
        if i % 2 == 1:
            if sumodd <= 0:
                cntodd += abs(sumodd) + 1
                sumodd += abs(sumodd) + 1
        else:
            if sumodd >= 0:
                cntodd += (sumodd + 1)
                sumodd -= (sumodd + 1)

    print(min(cnteven, cntodd))
#    print(cnteven, cntodd)

resolve()