from sys import *

a, b, c = map(int, stdin.readline().split())
ans = c - (a - b)
print(max(0, ans))