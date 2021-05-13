from sys import stdin
a = int(stdin.readline().rstrip())
b = int(stdin.readline().rstrip())
c = int(stdin.readline().rstrip())
x = int(stdin.readline().rstrip())
y = 0

for p in range(a+1):
   if 500*p > x:
      break
   for q in range(b+1):
      if 500*p + 100*q > x:
         break
      for r in range(c+1):
         if 500*p + 100*q + 50*r > x:
            break
         if 500*p + 100*q + 50*r == x:
            y += 1

print(y)