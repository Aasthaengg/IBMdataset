from collections import *
from itertools import *

N,M=map(int,input().split())
A=list(map(int,input().split()))

s=[0]+list(accumulate(A))
for i in range(len(s)):
  s[i]%=M
s_cnt=Counter(s)

ans=0
for x in s_cnt.values():
  ans+=x*(x-1)//2

print(ans)
