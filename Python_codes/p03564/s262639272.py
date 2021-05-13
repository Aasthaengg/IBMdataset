N = int(input())
K = int(input())
res = 1
for i in range(N):
  if res < K:
    res = res *2
  else:
    res = res + K
print(res)