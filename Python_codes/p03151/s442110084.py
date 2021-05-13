n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=[a[i]-b[i] for i in range(n)]
if sum(x)<0:
  print(-1)
  exit()
x.sort()
if x[0]>=0:
  print(0)
  exit()
ans=0
m=0
while x[ans]<0:
  ans+=1
m=sum(x[:ans])
x=x[ans:][::-1]
i=0
while True:
  m+=x[i]
  i+=1
  if m>0:
    break
ans+=i
print(ans)