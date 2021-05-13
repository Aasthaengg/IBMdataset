n = int(input())

a = [int(input())-1 for _ in range(n)]

flag = False
index = 0
count = 0

for i in range(n):
  index = a[index]
  count += 1
  if index == 1 :
    flag = True
    break

if flag:
  print(count)
else:
  print(-1)
