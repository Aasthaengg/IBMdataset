n = int(input())
lst = list(map(int, input().split()))
dic = {0:0, 1:0, 2:0}
for i in range(n):
  if lst[i] % 4 == 0:
    dic[2] += 1
  elif lst[i] % 2 == 0:
    dic[1] += 1
  else:
    dic[0] += 1
pre = 2
for i in range(n):
  if pre == 2:
    if dic[0] >= 1:
      dic[0] -= 1
      pre = 0
    else:
      print('Yes')
      exit()
  else:
    if dic[2] >= 1:
      dic[2] -= 1
      pre = 2
    else:
      print('No')
      exit()
print('Yes')