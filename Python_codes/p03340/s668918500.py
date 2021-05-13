n=int(input())
a=list(map(int,input().split()))
right,ans,sum_xor,sum=1,0,a[0],a[0]

for left in range(n):
  if left==right:
    right=left+1
    sum_xor^=a[left]
    sum+=a[left]
  while right<n and sum_xor^a[right]==sum+a[right]:
    sum_xor^=a[right]
    sum+=a[right]
    right+=1
  ans+=right-left
  sum_xor^=a[left]
  sum-=a[left]
print(ans)