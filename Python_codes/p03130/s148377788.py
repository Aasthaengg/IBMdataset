ret = []
for i in range(3):
  ret+=list(map(int,input().split()))
ret.sort()
if ret.count(1)==3 or ret.count(2)==3 or ret.count(3)==3 or ret.count(4)==3:
  print('NO')
else:
  print('YES')