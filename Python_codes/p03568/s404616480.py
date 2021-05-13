n=int(input())
a=[0]*n
a=list(map(int,input().split()))
ans=1
for i in range(n):
  if (a[i]%2==1):
    ans*=1
  else:
    ans*=2
    
print(3**n-ans)