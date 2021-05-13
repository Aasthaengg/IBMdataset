from collections import Counter 
n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))
for i in range(n):
  a[i+1]+=a[i]
  a[i+1]%=m
a=list(Counter(a).values())
ans=0
for i in a:
  ans+=i*(i-1)//2
print(ans)