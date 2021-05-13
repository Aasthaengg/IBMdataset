#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

"""
[解説AC]
1. k>=2**mのとき
明らかに-1
2. m=0のとき
同じ数2つなのでxorは必ず0
3. m=1のとき
k=0なら2種類の数を2つずつ並べる
k!=0なら2種類の数2つずつの並べ方はk=0の場合の並べ方以外で
2種類(交互に並べる,片方の種類の数の間にもう一方の数2枚)
交互に並べる場合,明らかにxorが異なる⇒×
片方の種類の数の間にもう一方の数2枚,明らかにxor=0になる⇒×
つまり、k!=0のとき-1
4.m>=2のとき
k以外の0以上2**m未満の数を昇順に並べる⇒bとする
k以外の0以上2**m未満の数を降順に並べる⇒cとする
bkckと並べると常にxor=kを満たす
k以外の0以上2**m未満の数の任意の数について、その間にはkが1つと
他の数が常に2つずつ入っている⇒xorは必ずk
kについて、間にはcがあるが、cはk以外の0以上2**m未満の数であり、
kが2つとc⇒0以上の2**未満の数とkのxor
0以上2**m未満の数については(2**m)-1が偶数個作れるため0であり、0xork=k
"""

m,k = LI()

if k >= 2**m:
    print(-1)
    quit()
if m == 0:
    if k == 0:
        print(0,0)
    else:
        print(-1)
elif m == 1:
    if k == 0:
        ans = [i for i in range(2**(m+1))]
        ans = [i//2 for i in ans]
        print(*ans)
    else:
        print(-1)
else:
    ans = [i for i in range(2**m) if i != k]
    ans = ans + [k] + ans[::-1] + [k]
    print(*ans)