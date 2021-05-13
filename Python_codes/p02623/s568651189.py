from bisect import *
from itertools import *
N,M,K = map(int,input().split())
A = [0]+list(accumulate(map(int,input().split())))
B = [0]+list(accumulate(map(int,input().split())))
ans = [0]

for n in range(1+N):
  C = bisect_right(B,K-A[n])-1
  if C!=-1:
    ans+=[C+n]

print(max(ans))