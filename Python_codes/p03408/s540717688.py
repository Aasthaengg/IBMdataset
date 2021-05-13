N=int(input())
b=[]
for _ in range(N):
  b.append(input())
M=int(input())
r=[]
for _ in range(M):
  r.append(input())

from collections import Counter
red=Counter(r)
blue=Counter(b)
ans=0
for k, v in blue.items():
  ans=max(ans, v-red[k])
print(ans)