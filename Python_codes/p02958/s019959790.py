n = int(input())
p = list(map(int,input().split()))
n_l = list(range(1,n + 1))
count = 0
for n_num , p_num in zip(n_l,p):
  if n_num != p_num:
    count += 1
if count == 2 or count == 0:
  print('YES')
else:
  print('NO')