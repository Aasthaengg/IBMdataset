import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

A, B, K = map(int, input().split())

l = []
for i in range(A, min(A+K, B+1)):
    l.append(i)
for i in range(max(B-K+1, A+1), B+1):
    l.append(i)

l = list(set(l))
l.sort()
print(*l, sep="\n")
