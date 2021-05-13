n,h=map(int,input().split())
ab=sorted([list(map(int,input().split())) for _ in range(n)],key=lambda x:x[1],reverse=True)
m=max([i[0] for i in ab])
ans=0
for i in ab:
  if i[1]>m:
    h-=i[1]
    ans+=1
    if h<=0:
      print(ans)
      exit()
if h%m==0:
  print(ans+h//m)
else:
  print(ans+h//m+1)