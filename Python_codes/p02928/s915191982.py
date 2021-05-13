n,k = map(int,input().split())
a = list(map(int,input().split()))
a *= 2
mod = 10**9+7
c = 0
d = 0
for i in range(n):
  for j in range(i+1,2*n):
    if a[i] > a[j]:
      if j >= n:
        d += 1
      else:
        c += 1
c = c*k%mod
d = d*k*(k-1)//2%mod
print((c+d)%mod)