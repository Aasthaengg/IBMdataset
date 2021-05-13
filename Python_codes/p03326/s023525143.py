import sys
from functools import lru_cache
import itertools
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m=map(int, readline().split())
ls=[[0 for i in range(n)] for j in range(8)]
p=list(itertools.product([1,-1],repeat=3))
for k in range(n):
  a=tuple(map(int, readline().split()))
  for j, i in enumerate(p):
    ls[j][k]=a[0]*i[0]+a[1]*i[1]+a[2]*i[2]
sum=[]
for i in range(8):
    sum.append(0)
    ls[i]=sorted(ls[i])
    for j in range(1,m+1):
        sum[i]+=ls[i][-j]
#print(ls)
#print(sum)
print(max(sum))