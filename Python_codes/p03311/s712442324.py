n=int(input())
a=list(map(int,input().split()))
for i in range(n):
  a[i]-=i+1
b=a[:]
b.sort()
mid1=0
mid2=0
if n%2==1:
  ans=0
  mid1=b[n//2]
  for bb in b:
    ans+=abs(bb-mid1)
  print(ans)
else:
  mid1=b[n//2]
  mid2=b[n//2-1]
  ans1,ans2=0,0
  for bb in b:
    ans1+=abs(bb-mid1)
    ans2+=abs(bb-mid2)
  print(min(ans1,ans2))
