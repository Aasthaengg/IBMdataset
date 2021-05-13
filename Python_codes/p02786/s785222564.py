H=int(input())
res = 0
i = 1
while H > 0:
  res += i
  H = H // 2
  i = i*2
print(res)