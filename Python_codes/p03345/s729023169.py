from sys import stdin
import math

a,b,c,k = [int(x) for x in stdin.readline().strip().split()]
print(((-1)**k) * (a - b))