import sys
import heapq


input = sys.stdin.readline
N, M, K = map(int, input().split())

for k in range(N+1):
    for l in range(M+1):
        if k*(M-l) + l*(N-k) == K:
            print("Yes")
            exit(0)

print("No")
