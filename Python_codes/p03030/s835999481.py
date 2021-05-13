n = int(input())

res = []
for i in range(n):
  city, value = input().split()
  value = int(value)
  res.append([city, value, i+1])
res_s = sorted(res, key = lambda x: (x[0], -x[1]))
for i in range(n):
  print(res_s[i][2])
