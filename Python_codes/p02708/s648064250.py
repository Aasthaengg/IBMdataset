n,k = map(int,input().split())

mod = 10**9 + 7

ans = 0
for i in range(k,n+2):
  min = i*(i-1)//2
  max = (n+1)*n//2 - (n+1-i)*(n-i)//2
  ans += (max - min + 1)%mod
print(ans%mod)