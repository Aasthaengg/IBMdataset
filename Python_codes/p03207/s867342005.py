n = int(input())
l = []
sum = 0
for i in range(n):
  x = int(input())
  sum += x
  l.append(x)
print(sum-(max(l)//2))