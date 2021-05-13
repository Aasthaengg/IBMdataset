n=int(input())
P=list(map(int,input().split()))
ans=0
for i in range(1,n-1):
  if P[i]<P[i-1] and P[i]>=P[i+1]:
    ans+=1
  elif P[i]<P[i+1] and P[i]>=P[i-1]:
    ans+=1
  else:
    continue

print(ans)
