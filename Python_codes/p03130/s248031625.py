count_list = [0,0,0,0]
for i in range(3):
  dis = [int(i) for i in input().split()]
  for j in dis:
    count_list[j-1] += 1

if max(count_list) >= 3:
  print('NO')
else:
  print('YES')