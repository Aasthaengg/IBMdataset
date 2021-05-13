N=int(input())
h=list(map(int,input().split()))
ans=0
flag=True
for i in range(N):
  for j in range(h[i]):
    for k in range(i,N):
      if h[k]==0:
        if k==i:
          flag=False
        break
      h[k]-=1
    if flag:
      ans+=1
    flag=True
print(ans)