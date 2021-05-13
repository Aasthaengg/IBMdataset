from sys import stdin

a, b = [int(x) for x in stdin.readline().rstrip().split()]
c = (a*b) % 2

if c == 1:
  print("Odd")
else:
  print("Even")