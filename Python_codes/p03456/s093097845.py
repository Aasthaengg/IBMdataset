a, b = map(str, input().split())
num = int(a + b)

for i in range(num):
  sqrt = i * i
  if sqrt > num:
    print('No')
    break
  elif sqrt == num:
    print('Yes')
    break
  else:
    pass