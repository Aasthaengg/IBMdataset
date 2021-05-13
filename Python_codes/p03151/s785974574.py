n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
suma=sum(a)
sumb=sum(b)
if suma<sumb:
  print(-1)
  exit()
d=[]
for i in range(n):
  d.append(a[i]-b[i])
d.sort()
import bisect
minus=bisect.bisect_left(d,0)
sum_minus=sum(d[:minus])
sum_plus=0
ans=minus
i=1
while sum_plus < -sum_minus:
  sum_plus+=d[-i]
  ans+=1
  i+=1
print(ans)
