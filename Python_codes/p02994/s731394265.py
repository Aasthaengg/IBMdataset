n, l = map(int, input().split())
taste = [l+i for i in range(n)]
tmp = 9999
index = 0
for i in range(n):
  if abs(taste[i]) < tmp:
    tmp = abs(taste[i])
    index = i
res = sum(taste) - taste[index]
print(res)