X = int(input())
c = 100
t = 0
while c < X:
  c += c // 100
  t += 1
print(t)