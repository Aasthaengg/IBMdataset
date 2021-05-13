n = int(input())
t = [0]
x = [0]
y = [0]
for i in range(n):
  t_, x_, y_ = map(int, input().split())
  t.append(t_)
  x.append(x_)
  y.append(y_)

for j in range(n):
  dt = t[j+1] - t[j]
  dx = abs(x[j+1] - x[j])
  dy = abs(y[j+1] - y[j])
  if dx+dy>dt or dt%2!=(dx+dy)%2:
    print('No')
    exit()
    
print('Yes')