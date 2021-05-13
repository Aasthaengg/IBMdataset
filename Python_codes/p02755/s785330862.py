a, b = map(int, input().split())
flag = False
for i in range(1300):
  if i * 8 // 100 == a and i * 10 // 100 == b:
    flag = True
    break
if flag:
  print(i)
else:
  print(-1)