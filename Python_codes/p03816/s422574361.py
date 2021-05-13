n=int(input())
a=list(map(int,input().split()))
d=[0]*(10**5+1)
sa=set(a)
for i in a:
  d[i]+=1
for j in range(len(d)):
  if d[j]>2 and d[j]%2==0:
    d[j]=2
  elif d[j]>2 and d[j]%2!=0:
    d[j]=1
ni=d.count(2)
if ni%2==0:
  print(len(sa))
else:
  print(len(sa)-1)