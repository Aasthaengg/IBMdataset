import math
import sys

n = int(sys.stdin.readline().rstrip())

if n == 1:
    print(1)
    sys.exit()
elif n == 2:
    print(2)
    sys.exit()

m = 1
s = 0
while (s <= n):
    s += m
    m += 1
# print(m)
for i in range(1, m):
    if i == s - n:
        continue
    else:
        print(i)