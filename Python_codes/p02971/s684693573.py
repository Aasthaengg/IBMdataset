n = int(input())
a = [int(input()) for _ in range(n)]

l = sorted(a, reverse=True)
x = l[0]
y = l[1]
for i in a:
  if i != x: print(x)
  else: print(y)