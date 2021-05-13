n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10**9+7
cnt = 0
for i in range(n):
  for j in range(i+1,n):
      if a[i] > a[j]:
        cnt += 1
ans = cnt*k
cnt2 = 0
for i in range(n):
  for j in range(n):
    if a[i] > a[j]:
      cnt2 += 1
ans += (k*(k-1)//2)*cnt2
print (ans%mod)