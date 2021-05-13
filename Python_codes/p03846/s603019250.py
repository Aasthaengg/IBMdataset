n=int(input())
a=list(map(int,input().split()))
if n%2==0:
  b=sorted([2*i+1 for i in range((n+1)//2)]*2)
else:
  b=sorted([2*i for i in range(1,(n+1)//2)]*2+[0])

if sorted(a)!=b:
  ans=0
else:
  ans=2**(n//2)
print(ans%(10**9+7))