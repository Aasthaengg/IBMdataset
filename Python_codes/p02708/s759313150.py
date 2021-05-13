n,k = map(int,input().split())
su = 0
mod = 10**9+7
for i in range(k,n+2):
  a = i*(i-1)//2
  b = i*(2*n+1-i)//2
  su += b-a+1
 # print(a,b,su)
  su %= mod
print(su)