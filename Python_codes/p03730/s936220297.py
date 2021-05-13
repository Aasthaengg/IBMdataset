MM = input().split()
A = int(MM[0])
B = int(MM[1])
C = int(MM[2])
count = 0
for i in range(1,B):
  if A*i%B ==C:
    count +=1
if count ==0:
  print('NO')
else:
  print('YES')