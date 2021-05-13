N = int(input())
p = [int(input()) for _ in range(N)]
q = [0] * (N + 1)
for i in range(N):
  q[p[i]] = i
res = 0
temp = 0
for i in range(2, N + 1):
  if q[i - 1]  < q[i]:
    temp += 1
  else:
    res = max(res, temp)
    temp = 0
res = max(res, temp)
print(N - res - 1)