a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

s = a+v*t
u = b+w*t
ss = a - v*t
uu = b - w*t

if b >= a:
  if s >= u:
    print ('YES')
  else:
    print ('NO')
else:
  if ss <= uu:
    print ('YES')
  else:
    print ('NO')