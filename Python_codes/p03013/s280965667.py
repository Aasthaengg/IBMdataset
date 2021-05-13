n, m = map(int, input().split())
mod = 10**9+7
ans = [1,1]
for i in range(2,100001):
  ans.append((ans[i-1]+ans[i-2])%mod)
num = 1
s = 0
for i in range(m):
  e = int(input())
  if e-1 < s:
    print(0)
    exit(0)
  num*=ans[e-1-s]
  num%=mod
  s = e+1
num*=ans[n-s]
print(num%mod)