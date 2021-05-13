from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations # (string,3) 3回
from collections import deque
from collections import defaultdict
import bisect
#
#    d = m - k[i] - k[j]
#    if kk[bisect.bisect_right(kk,d) - 1] == d:
#
#
#
# pythonで無理なときは、pypyでやると正解するかも！！
#
#

import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7

def readInts():
  return list(map(int,input().split()))
def main():
    a,b,q = readInts()
    S = [-float("inf")] + [int(input()) for _ in range(a)] + [float("inf")]
    #S = sorted(S)
    T = [-float("inf")] + [int(input()) for _ in range(b)] + [float("inf")]
    for i in range(q):
        ans = float("inf")
        x = int(input())
        Sl = bisect.bisect_left(S,x)
        Tl = bisect.bisect_left(T,x)
        # 4通り試して一番小さいもの!!
        for s in (S[Sl-1],S[Sl]):
            for t in (T[Tl-1],T[Tl]):
                # 最小値、いったんsに行ってs-t, いったんtに行ってt-s で最小値を求める
                ans = min(ans,abs(s-x) + abs(s-t),abs(t-x)+abs(s-t))
        print(ans)
    # print(ans)
    #T = sorted(T)
    # for i in range(q):
    #     x = int(input())
    #     ans = 0
    #     now = x
    #     Sa = float("inf")
    #     Ta = float("inf")
    #     Sidx = bisect.bisect_right(S,x)
    #     Tidx = bisect.bisect_right(T,x)
    #     #print("-!-",x,Sidx,S)
    #     #print("-?-",x,Tidx,T)
    #     # ------------------------------------
    #     if Sidx < len(S):
    #         Sa = abs(S[Sidx] - x)
    #         Si = Sidx
    #     if Sidx - 1 >= 0:
    #         if Sa > abs(S[Sidx-1] - x):
    #             Sa = abs(S[Sidx-1] - x)
    #             Si = Sidx - 1
    #     # ------------------------------------
    #     if Tidx < len(T):
    #         if Ta > abs(T[Tidx] - x):
    #             Ta = abs(T[Tidx] - x)
    #             Ti = Tidx
    #     if Tidx - 1 >= 0:
    #         if Ta > abs(T[Tidx-1] - x):
    #             Ta = abs(T[Tidx-1] - x)
    #             Ti = Tidx - 1
    #     # ------------------------------------
    #     print(S,S[Si])
    #     print(T,T[Ti])
    #     mid = abs((S[Si] - T[Ti]))
    #     if abs(mid + Sa) < abs(mid + Ta):
    #         now = S[Si]
    #         ans += Sa
    #         jin = False
    #     else:
    #         print('?')
    #         if Ti - 1 >= 0:
    #             t =
    #             now = T[Ti]
    #             ans += Ta
    #             jin = True
    #     mi_ = float("inf")
    #     if jin:# 次神社を調べろ
    #         Sidx = bisect.bisect_right(S,now)
    #         if Sidx < len(S):
    #             mi_ = abs(now - S[Sidx])
    #         if Sidx - 1 >= 0:
    #             mi_ = min(mi_, abs(now - S[Sidx-1]))
    #         ans += mi_
    #     else:
    #         Tidx = bisect.bisect_right(T,now)
    #         if Tidx < len(T):
    #             mi_ = abs(now - T[Tidx])
    #         if Tidx - 1 >= 0:
    #             mi_ = min(mi_, abs(now - T[Tidx-1]))
    #         ans += mi_
    #     print(ans)
    #     print("--next--")

if __name__ == '__main__':
  main()
