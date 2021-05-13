arr=[]
for i in range(3):
  a,b=map(int,input().split())
  arr.append(a)
  arr.append(b)
if arr.count(1)==3 or arr.count(2)==3 or arr.count(3)==3 or arr.count(4)==3:
  print('NO')
else:
  print('YES')