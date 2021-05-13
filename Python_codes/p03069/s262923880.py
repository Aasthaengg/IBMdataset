import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    N = int(input())
    S = list(input())
    bl = [0]*N
    wh = [0]*N

    from itertools import accumulate

    wh_num = 0
    for i in range(N):
        if S[i] == '#':
            bl[i] = 1
        else:
            wh[i] = 1

    bl = [0] + bl
    wh = [0]+wh

    # 累積和を格納したリスト．A[l:r]の総和はB[r] - B[l]
    bl = list(accumulate(bl))
    wh = list(accumulate(wh))

    # この問題は長さが1-Nの連続部分の和の最大値を出せというものなので以下の通り
    ans = N
    for i in range(N + 1):
        ans = min(ans, bl[i]+(wh[N]-wh[i]))
    print(ans)


resolve()