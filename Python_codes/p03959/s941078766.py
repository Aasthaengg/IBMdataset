n=int(input())
ht=list(map(int,input().split()))
ha=list(map(int,input().split()))
ans=ha[0]==ht[-1] and ha[ht.index(ht[-1])]==ht[-1]
m=10**9+7
cnt=0
for i,(t,a) in enumerate(zip(ht[1:n-1],ha[1:n-1])):
  if t<a and t==ht[i]:ans*=t
  elif t>a and a==ha[i+2]:ans*=a
  cnt+=t==a
  ans%=m
cnt+=(ha[0]==ht[0])+(ha[-1]==ht[-1])
ans*=pow(max(ha),max(cnt-2,0),m)
print(ans%m)