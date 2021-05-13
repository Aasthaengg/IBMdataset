n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if sum(a)<sum(b):
  print(-1)
  exit()
ans=0
ab=[]
cd=[]
for i in range(n):
  m=a[i]-b[i]
  if m<0:
    ab.append(m)
  else:
    cd.append(m)
res=sum(ab)
cd.sort(reverse=True)
t=0
if len(ab)>0:
  while t<len(cd):
    res+=cd[t]
    t+=1
    if res>0:
      print(len(ab)+t)
      exit()
else:
  print(0)