n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
ans=0
for i in range(n):
  if l1[i]>=l2[i]:
    ans+=l1[i]-l2[i]
print(ans)