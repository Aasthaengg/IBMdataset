
import sys
def input():
	return sys.stdin.readline().strip()

N, K = list(map(int, input().split()))

if K % 2 == 0:
	x = N // (K // 2)
	x2 = x//2
	x = x - x2
	print(x2**3 + x**3)
else:
	x = N // K
	print(x**3)