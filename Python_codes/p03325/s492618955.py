N=int(input())
W=list(map(int,input().split()))
even=[]
for i in range(N):
  if W[i]%2==0:
    even.append(W[i])
ans=0
for j in range(len(even)):
  while even[j]%2==0:
    even[j]=even[j]/2
    ans+=1
print(ans)
