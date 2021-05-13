A = list(map(int, input().split()))
li = [0] * 10
for i in A:
  li[i] += 1
if(li[1] == li[9] == li[7] == li[4] == 1):
  print('YES')
else:
  print('NO')