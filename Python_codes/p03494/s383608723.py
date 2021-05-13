from sys import stdin
n = stdin.readline().rstrip()
a = [int(x) for x in stdin.readline().rstrip().split()]
b = 0

while True:
   if all([x % 2 == 0 for x in a]):
      a = [x/2 for x in a]
      b += 1
   else:
      break

print(b)