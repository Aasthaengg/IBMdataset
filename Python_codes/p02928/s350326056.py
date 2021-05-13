from sys import stdin
from collections import defaultdict, deque, Counter
import sys
from bisect import bisect_left
import heapq
import math

sys.setrecursionlimit(10000000)
MIN = -10 ** 9
MOD = 10 ** 9 + 7
INF = float("inf")
IINF = 10 ** 18

#n = int(stdin.readline().rstrip())
#l = list(map(int, stdin.readline().rstrip().split()))
n,k = map(int, stdin.readline().rstrip().split())
#S = [list(stdin.buffer.readline().decode().rstrip()) for _ in range(h)]
A = list(map(int, stdin.readline().rstrip().split()))



ans = 0
for i in range(n):
    right = 0
    left = 0
    for j in range(i):
        if A[i] > A[j]:
            left += 1
    for j in range(i+1, n):
        if A[i] > A[j]:
            right += 1
    ans += int(right*k*(k+1)//2 + left*k*(k-1)//2)

print(ans % MOD)
