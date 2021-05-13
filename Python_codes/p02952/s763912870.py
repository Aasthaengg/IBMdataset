import sys, math
from collections import defaultdict
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 1000000007
sys.setrecursionlimit(1000000)

N = ri()

ans = 0
for i in range(1, N+1):
	if len(list(str(i))) % 2 == 1:
		ans += 1
print(ans)
