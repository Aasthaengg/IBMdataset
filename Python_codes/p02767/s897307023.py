n = int(input())
x = [int(x) for x in input().split()]
res = 10 ** 10
for i in range(101):
  c = 0
  for j in range(n):
    c += (i - x[j]) ** 2
  res = min(res,c)
print(res)