import sys
from collections import Counter
from collections import deque
import heapq
import math
import fractions
import bisect
import itertools
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n=int(input())
sosuu = [2]
A = 5555
for L in range(3, A, 2): # 2 以外の素数は奇数なので
    for L2 in sosuu:
        if L % L2 == 0:
            break # 素数でないことがわかったらそれ以上ループする必要はない
    else: # break で抜けることがなかったら L は素数（Python 特有の制御構文）
        sosuu.append(L)
ans=[]
count=0
for i in sosuu:
    if i%5==1:
        count+=1
        ans.append(i)
    if count==n:
        print(*ans)
        exit()