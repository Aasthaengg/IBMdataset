n=int(input())
h=[int(x) for x in input().split()]
ans=0
c=0
for i in range(n-1):
  if h[i]>=h[i+1]:
    c+=1
  else:
    ans=max(ans,c)
    c=0
ans=max(ans,c)
print(ans)