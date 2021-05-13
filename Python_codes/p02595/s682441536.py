a,b = map(int,input().split())
xy = [map(int, input().split()) for _ in range(a)]
x, y = [list(i) for i in zip(*xy)]
c = 0

for j in range(a):
  if (x[j])**2 + (y[j])**2 <= b**2:
    c += 1
print(str(c))