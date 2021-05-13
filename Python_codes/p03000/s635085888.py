n,x = map(int, input().split())
l = input().split()
c = 1
d = 0
for i in range(n):
  d += int(l[i])
  if d <= x:
    c += 1
print(c)