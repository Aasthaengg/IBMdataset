N = int(input())
a = [int(s) for s in input().split()]
b = int(1)
flag = int(0)
flag2 = int(0)

#0がないか確認する
for i in range(N):
  if a[i] == 0:
    flag = 1
    break
  else:
    pass

for i in range(N):
  b = b * a[i]
  if b > 1000000000000000000:
    flag2 = 1
    break
  else:
    pass

if flag == 1:
  print("0")
elif flag2 == 1:
  print("-1")
else:
  print(int(b))
