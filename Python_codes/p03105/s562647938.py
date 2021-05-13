a, b, c = map(int, input().split())
d = 0
for i in range(1,c+1):
  if i*a <=b:
    d += 1
    continue
  else:
    break
print(d)