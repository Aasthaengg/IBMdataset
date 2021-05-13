a, b, c = map(int, input().split())

now = a
#loop = 2
check = 0

for i in range(1000000):
#  print(now, now//a,  b, now%b)
  if now % b == c:
    check += 1
    break
  else:
#    now += a*loop
    now += a
#    loop += 1
    
if check > 0:
  print('YES')
else:
  print('NO')