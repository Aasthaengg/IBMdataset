N,A,B = map(int,input().split())

if abs(A - B) % 2 == 0:
  ans = 'Alice'
else:
  ans = 'Borys'

print(ans)