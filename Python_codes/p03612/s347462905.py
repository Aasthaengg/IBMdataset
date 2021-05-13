n=int(input())
p=list(map(int,input().split()))
ans=0
cnt=0
sw=None
for i in range(n):
  if sw==None:
    if i+1==p[i]:
      sw=True
      cnt=p[i]
      ans+=1
  else:
    sw=None
print(ans)