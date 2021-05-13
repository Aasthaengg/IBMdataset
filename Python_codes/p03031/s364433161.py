import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n,m=mp()
s=[]
for i in range(m):
    s.append(lmp())
p=lmp()
ans=0
for i in range(2**n):#全てのスイッチの入れ方
    ans+=1
    for j in range(m):#全ての電球に対するチェック
        c=0
        for k in range(1,s[j][0]+1):#各電球に対するチェック
            if ((i>>(s[j][k]-1)) & 1):
                c+=1
        if (c-p[j])%2==1:
            ans-=1
            break
print(ans)