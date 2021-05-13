from sys import stdin, stdout, setrecursionlimit
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
import math

rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()	
rli = lambda: map(int, stdin.readline().split())
rlf = lambda: map(float, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')

def main():
	n, k = rli()
	A = list(math.log(x) for x in rli())
	prev, score = 1, 1
	for i, a in enumerate(A):
		prev = score
		score += a 
		if i >= k:
			score -= A[i-k]
			if score > prev:
				print("Yes")
			else:
				print("No")
	stdout.close()

if __name__ == "__main__":
	main()