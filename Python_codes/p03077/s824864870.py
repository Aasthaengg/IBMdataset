from math import *

n = int(input())
t = [int(input()) for _ in range(5)]

print(ceil(n / min(t)) + 4)