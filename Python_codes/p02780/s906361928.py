n,k=map(int, input().split())
p=list(map(int, input().split()))
num=sum(p[0:k])
ans=num
for i in range(n-k):
  num=num-p[i]+p[i+k]
  ans=max(ans,num)
print((ans+k)/2)