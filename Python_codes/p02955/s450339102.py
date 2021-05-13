import sys, math
from collections import defaultdict
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 1000000007
sys.setrecursionlimit(1000000)

N, K = rl()
A = rl()

s = sum(A)
m = math.ceil(math.sqrt(s))

divs = []
divs2 = []
i = 1
while i <= m:
	if s % i == 0:
		divs.append(i)
		divs2.append(s//i)
	i += 1
divs.reverse()
divs2 += divs

ans = 1
for n in divs2:
	B = [a % n for a in A]
	s = sum(B)
	if s % n != 0: continue
	B.sort()
	B = [b for b in B if b != 0]
	if len(B) == 0:
		ans = max(ans, n)
		break
	bsum = [0]*len(B)
	rbsum = [0]*len(B)
	bs = 0
	for i, b in enumerate(B):
		bs += b
		bsum[i] = bs
	bs = 0
	for i in range(len(B)-1, -1, -1):
		bs += n - B[i]
		rbsum[i] = bs
	need = float('inf')
	for i in range(len(B)-1):
		if bsum[i] == rbsum[i+1]:
			need = bsum[i]
			break
	if need <= K:
		ans = max(ans, n)
		break
print(ans)

