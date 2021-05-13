n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
mod = 10**9+7
if (max(a) < 0 and k%2) or n == k:
  ans = 1
  for i in range(n-k,n):
    ans *= a[i]
    ans %= mod
  print(ans)
  exit()
cntn = 0
cntp = n-1
if k%2:
  ans = a[-1]
  cntp -= 1
  n -= 1
else:
  ans = 1
for i in range(k//2):
  tmp = 0
  if (cntn < n-1 and a[cntn+1] < 0) and (cntp > 0 and a[cntp-1] >= 0):
    if a[cntn]*a[cntn+1] > a[cntp-1]*a[cntp]:
      tmp = a[cntn]*a[cntn+1]
      cntn += 2
    else:
      tmp = a[cntp-1]*a[cntp]
      cntp -= 2
  elif cntn < n-1 and a[cntn+1] < 0:
    tmp = a[cntn]*a[cntn+1]
    cntn += 2
  else:
    tmp = a[cntp-1]*a[cntp]
    cntp -= 2  
  ans *= tmp
  ans %= mod
print(ans)