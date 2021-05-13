a,b,c = map(int, input().split())
x = 0

for i in range(a,b):
 if c % i == 0:
  x += 1

if c % b == 0:
 x += 1

print(x)
