N = int(input())
t = []
x = []
y = []
for i in range(N):
  a,b,c = map(int, input().split())
  t.append(a)
  x.append(b)
  y.append(c)

def helper():
  curt = 0
  curx = 0
  cury = 0
  for i in range(N):
    dt = t[i] - curt
    curt = t[i]

    dx = abs(x[i] - curx)
    curx = x[i]

    dy = abs(y[i] - cury)
    cury = y[i]

    if dt < (dx+dy) or dt%2 != (dx+dy)%2:
      return False
  return True

a = helper()  
print('Yes') if a else print('No')
