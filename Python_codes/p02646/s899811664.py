a = list(map(int, input().split()))
b = list(map(int, input().split()))
t = int(input())

if b[1]-a[1]>0:
  print('NO')
else:
  if abs(a[0]-b[0])>(a[1]-b[1])*t:
    print('NO')
  else:
    print('YES')