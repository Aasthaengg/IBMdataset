import sys

read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines


# mod=10**9+7
# rstrip().decode('utf-8')
# map(int,input().split())
import numpy as np

def main():
	N, K,*A = map(int, read().split())
	a = np.array(A,dtype=np.int64)
	ans = 0
	for i in range(50, -1, -1):
		s = np.sum((a >> i) & 1)
		#print((a >> i)&1)
		if N - s > s:
			ans += 1<<i
		if ans > K:
			ans -= 1<<i
		#print(ans)
	print(np.sum(ans ^ a))


if __name__ == "__main__":
	main()
