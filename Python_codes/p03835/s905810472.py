k, s = map(int, input().split())
cnt = 0
for i in range(k+1):
  for j in range(k+1):
    if max(0, s-k) <= i+j <= s:
      cnt += 1
    elif i + j > s:
      break
print(cnt)
