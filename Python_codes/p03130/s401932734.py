ab = [[int(i) for i in input().split()] for _ in range(3)]

cnt = [0] * 4
for a, b in ab :
  cnt[a-1] += 1
  cnt[b-1] += 1
  
if cnt.count(1) == cnt.count(2) == 2 :
  print('YES')
else :
  print('NO')