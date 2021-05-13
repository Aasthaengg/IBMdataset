n, a, b = map(int, input().split())
x = 0
for i in range(1,n+1):
  y = list(str(i))
  z = [int(x) for x in y]
  if a <= sum(z) <= b:
    x += i
print(x)