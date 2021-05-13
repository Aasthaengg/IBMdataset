a,b = [int(x) for x in input().split()]
res = -1
for i in range(20000):
  if i * 8 // 100 == a and i * 10 // 100 == b:
    res = i
    break
print(res)