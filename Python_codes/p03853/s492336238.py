import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

H, W = map(int, input().split())

for _ in range(H):
    l = input()
    print(l)
    print(l)
