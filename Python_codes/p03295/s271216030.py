N,M=map(int,input().split())
a=[list(map(int,input().split())) for i in range(M)]
a.sort(key=lambda x:x[1])
j=0
k=0
ans=0
for i in range(M):
  if i==0:
    k=a[i][1]
    j=k-1
    ans+=1
  else:
    if a[i][0]<=j:
      continue
    else:
      k=a[i][1]
      j=k-1
      ans+=1
print(ans)