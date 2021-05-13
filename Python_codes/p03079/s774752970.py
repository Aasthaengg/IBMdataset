import sys

z = sys.stdin.readline()
a, b, c = int(z.split(" ")[0]), int(z.split(" ")[1]), int(z.split(" ")[2])

if a == b and b == c:
  sys.stdout.write('Yes')
else:
  sys.stdout.write('No')