#! /usr/bin/env python3
import sys
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

N, *A = map(int, read().split())

if N == 0:
    acc = A[0]
    if acc == 1:
        print(1)
    else:
        print(-1)
    sys.exit()

inf = 1 << 60

bound = [0] * (N+1)
bound[0] = 1
flag = True
for i in range(1, N+1):
    bound[i] = min(inf, (bound[i-1] - A[i-1]) * 2)
    if bound[i] < A[i]:
        flag = False

if not flag:
    print(-1)
    sys.exit()

nodes = [0] * (N+2)
for i in range(N, -1, -1):
    acc = min(bound[i], nodes[i+1] + A[i])
    nodes[i] = acc

print(sum(nodes))
