n=int(input())
lst=list(map(int,input().split()))
ans=0
x=sum(lst)
true=10**16
for i in range(n-1):
  ans+=lst[i]
  x-=lst[i]
  true=min(true,abs(ans-x))
print(true)