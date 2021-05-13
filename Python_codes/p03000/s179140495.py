a, b = map(int, input().split())
L = list(map(int, input().split()))
x = [0]
y = 0
z = 0
for i in range(a):
  y = y + L[i]
  x.append(y)
for j in range(len(x)):
  if x[j] <= b:
    z = z+1
print(z)