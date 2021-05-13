n = int(input())
a = [int(input()) for _ in range(n)]
b = sorted(a)
for v in a:
  print(b[(v<b[-1])-2])