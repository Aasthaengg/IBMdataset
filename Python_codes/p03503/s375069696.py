import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    N = int(input())
    F = [list(map(int, input().split())) for i in range(N)]
    P = [list(map(int, input().split())) for i in range(N)]
    profit = -10**10
    # bit全探索
    # https://qiita.com/gogotealove/items/11f9e83218926211083a#%E4%BE%8B%E9%A1%8C-1
    n = 10
    # 昇順での探索だよ
    for i in range(1, 2 ** n):
        bag = [0] * N
        cnt = 0

        """        
        10進数表記　2進数表記
        0           000
        1           001
        2           010
        3           011
        4           100
        5           101
        6           110
        7           111
        """

        for j in range(n):  # このループが一番のポイント
            if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
                for k in range(N):
                    if F[k][j] == 1:
                        bag[k] += 1
        for l in range(N):
            cnt += P[l][bag[l]]
        profit = max(profit, cnt)
    print(profit)


resolve()