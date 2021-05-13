from sys import stdin

n, x = [int(x) for x in stdin.readline().split()]
a_lst = sorted([int(x) for x in stdin.readline().split()])
s = 0

for i, a in enumerate(a_lst):
  s += a
  if s > x:
    print(i)
    exit()
    
if s == x: print(i+1)
else: print(i)