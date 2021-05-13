X, Y = map(int,input().split())
a = Y - 2 * X
b = a / 2
c = int(b)
if b == c and 0 <= b and b <= X:
  print('Yes')
else:
  print('No')