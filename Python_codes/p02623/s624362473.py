n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
sa = [0]
sb = [0]
for i in range(n):
  sa.append(sa[i]+a[i])
for i in range(m):
  sb.append(sb[i]+b[i])
maxn = 0
j = m
for i in range(n+1):
  if sa[i] <= k:
    while sa[i] + sb[j] > k:
      j -= 1
    maxn = max(maxn,i+j)
print(maxn)