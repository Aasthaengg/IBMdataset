N = int(input())
A = list(map(int,input().split()))
A.sort()
import sys, copy, math, heapq, bisect
from itertools import accumulate
from collections import deque, defaultdict, Counter
input = sys.stdin.readline # 文字列の入力のとき'/n'まで受け取るので注意!!!
sys.setrecursionlimit(500000)
mod = 10**9+7
D = Counter(A)
if N%2==0:
    ans = 1
    for i,k in enumerate(D.keys()):
        if D[k]==2:
            ans = ans*2%mod
        else:
            ans = 0
            break
    print(ans)


else:
    ans = 1
    for i,k in enumerate(D.keys()):
        if i==0 and D[k]==1:
            continue
        elif i==0:
            ans = 0
            break
        elif D[k]==2:
            ans = ans*2%mod
        else:
            ans = 0
            break
    print(ans)




