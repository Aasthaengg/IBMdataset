N = int(input())
ans = 100
for i in range(1, N // 2 + 1):
  A = str(i)
  B = str(N - i)
  t = 0
  for j in A:
    t += int(j)
  for j in B:
    t += int(j)
  ans = min(ans, t)
print(ans)