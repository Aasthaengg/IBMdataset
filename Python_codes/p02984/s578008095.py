import sys, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from itertools import combinations, permutations, product
from heapq import heappush, heappop
from functools import lru_cache
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 1000000007
sys.setrecursionlimit(1000000)

N = ri()
A = rl()

sumA = sum(A)

even = [0]
s = 0
for i in range(N-1, -(2*N+4), -2):
	s += A[i%N]
	even.append(s)
odd = [0]
s = 0
for i in range(N-2, -(2*N+4), -2):
	s += A[i%N]
	odd.append(s)

B = [0] * N
for i in range(N):
	r = 0
	if i%2==0:
		r = even[N//2-i//2+N//2+1]-even[N//2-i//2]
	else:
		r = odd[N//2-1-(i-1)//2+N//2+1]-odd[N//2-1-(i-1)//2]
	B[i] = r - (sumA-r)
print(*([B[-1]]+B[:-1]))