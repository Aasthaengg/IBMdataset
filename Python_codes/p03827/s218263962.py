X = [0]
x = 0
n = int(input())
for s in input():
  if s=="I":
    x += 1
  else:
    x -= 1
  X.append(x)
print(max(X))