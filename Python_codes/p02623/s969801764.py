n, m, k = [int(i) for i in input().split()]
a = [0] + [int(i) for i in input().split()]
b = [0] + [int(i) for i in input().split()]
for i in range(1, n+1):
  a[i] += a[i-1]
for i in range(1, m+1):
  b[i] += b[i-1]
cnt, cnt_ = 0, 0
for i in range(n+1):
  if a[i] <= k:
    cnt = i
for j in range(m+1):
  if b[j] + a[cnt] <= k:
    cnt_ = j
ans = cnt + cnt_
for i in range(cnt):
  for j in range(cnt_, m+1):
    if a[cnt - i - 1] + b[j] > k:
      cnt_ = j
      break
    else:
      ans = max(ans, cnt - i - 1 + j)
print(ans)