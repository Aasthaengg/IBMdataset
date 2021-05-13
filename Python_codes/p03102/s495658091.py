n, m, c = map(int, input().split())
blst = list(map(int, input().split()))
res = 0
for i in range(n):
  temp = c
  alst = list(map(int, input().split()))
  for j in range(m):
    temp += (alst[j] * blst[j])
  if temp > 0:
    res += 1
print(res)