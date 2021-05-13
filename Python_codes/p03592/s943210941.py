import sys
from sys import stdin

n, m, k = map(int, stdin.readline().rstrip().split())
ans = 0
for i in range(n+1):
    for j in range(m+1):
        if i * m + j * n - i * j * 2 == k:
            print("Yes")
            sys.exit()

print('No')