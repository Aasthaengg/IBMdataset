n=int(input())
a=list(map(int,input().split()))
ans=0
i=1
while i<n:
  if a[i]==a[i-1]:
    ans=ans+1
    i=i+1
  i=i+1
print(ans)