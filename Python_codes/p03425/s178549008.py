from collections import defaultdict
import itertools
d = defaultdict(int)
x='MARCH'
for i in range(5):
  d[x[i]]=i+1
x=[0]*5
N=int(input())
for i in range(N):
  S=input()
  a=d[S[0]]
  if a>0:
    x[a-1]+=1
ans=0
for i,j,k in itertools.combinations([i for i in range(5)], 3):
  ans+=x[i]*x[j]*x[k]
print(ans)