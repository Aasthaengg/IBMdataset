from sys import stdin
from math import sin, cos, pi, sqrt

while True:
    n = int(stdin.readline().rstrip())
    if n == 0:
        break
    else:
        s = [int(x) for x in stdin.readline().rstrip().split()]
        ava = sum(s)/n
        alpha = sqrt(sum([(si-ava)**2 for si in s])/n)
        print(alpha)

