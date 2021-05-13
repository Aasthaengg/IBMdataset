a, b, k = map(int, input().split())

min = [0] * k
max = [0] * k

for i in range(k):
  if a+i > b:
    break
  min[i] = a+i

for n in range(k):
  if b-n < a:
    break
  max[n] = b-n

ans = min + max
ans = set(ans)
ans = list(ans)
ans.sort()

for j in ans:
  if j == 0:
    continue
  print(j)