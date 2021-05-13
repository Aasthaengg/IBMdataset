N = int(input())
t = [0]
x = [0]
y = [0]
for i in range(N):
  a,b,c = map(int, input().split())
  t.append(a)
  x.append(b)
  y.append(c)

def helper():
  for i in range(N):
    dt = t[i+1] -t[i] 
    dx = abs(x[i+1] - x[i])
    dy = abs(y[i+1] - y[i])

    if dt < (dx+dy) or dt%2 != (dx+dy)%2:

      return False
  return True

a = helper()  
print('Yes') if a else print('No')
