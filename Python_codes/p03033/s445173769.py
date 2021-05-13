import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N, Q = LI()
    sections = []
    D = []

    for _ in range(N):
        s, t, x = LI()
        s -= x
        t -= x
        sections.append((s, t, x))

    for _ in range(Q):
        D.append(I())
    sections = sorted(sections, key=lambda x: (x[-1], x[-2]))

    section_end_ix = collections.defaultdict(list)

    filled = [-1] * Q
    for sec in sections:
        l = bisect.bisect_left(D, sec[0])
        r = bisect.bisect_left(D, sec[1])
        x = sec[2]
        # 調整 [0, 2, 5, 8, 9]、区間[1, 5]のとき、l = 1, r = 3になる。r = 2にする。
        # 調整 [0, 2, 5, 8, 9]、区間[2, 4]のとき、l = 1, r = 2になる。r = 1にする。
        r -= 1
        if r < 0:
            continue
        section_end_ix[x].append(r)
        ix = l
        while ix <= r:
            val_X = filled[ix] # 進める距離
            # 既に埋まってたら終点までスキップ
            if val_X > -1:
                _i = bisect.bisect_left(section_end_ix[val_X], ix) # section_end_ix[val_X]: 進める距離の終点のindexがのった配列
                # ix = 4、section_end_ix[val_X] = [2, 4, 7]のとき、2がかえる。

                if _i >= len(section_end_ix[val_X]):
                    # かぶってないのでよい
                    pass
                else:
                    # 終点までスキップ
                    ix = section_end_ix[val_X][_i]
            # うまってなかったら埋める
            else:
                filled[ix] = x
            ix += 1

    for x in filled:
        print(x)
main()

