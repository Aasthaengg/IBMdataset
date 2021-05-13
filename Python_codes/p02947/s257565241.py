n=int(input())
b=[]
for _ in range(n):
  g=str(input())
  b.append(str(sorted(g)))
import collections
c = collections.Counter(b)
#print(c)
cnt=0
for i in c:
  cnt+=c[i]*(c[i]-1)/2
print(int(cnt))