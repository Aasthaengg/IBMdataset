import sys
from itertools import accumulate
input = sys.stdin.readline
def inputs():return [int(x) for x in input().split()]
N,C = inputs()
stc = [inputs() for i in range(N)]
stc = sorted(stc,key=lambda x:x[1])
stc = sorted(stc,key=lambda x:x[2])
ans = [0]*(10**5+2)
for i in range(N):
    s,t,c, = stc[i]
    if i>0 and c==stc[i-1][2] and s==stc[i-1][1]:
      ans[s+1]+=1
      ans[t+1]-=1
      continue
    ans[s]+=1
    ans[t+1]-=1
ans = list(accumulate(ans))
print(max(ans))