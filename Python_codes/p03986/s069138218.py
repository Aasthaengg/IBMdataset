X = str(input())

n = len(X)
tmp = 0
cnt = 0
for i in range(n):
  if X[n-1-i] == 'T':
    tmp += 1
  else:
    if tmp > 0:
      tmp -= 1
      cnt += 1

ans = n - 2*cnt
print(ans)