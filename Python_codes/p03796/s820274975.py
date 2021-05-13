n=int(input())


k=0
ans=1
w=10**9+7

for i in range(n):
  k = k+1
  ans*=k
  ans%=w

print(ans)