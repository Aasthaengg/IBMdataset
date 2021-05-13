import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

H, W = map(int, input().split())

print("#" * (W + 2))
for _ in range(H):
    line = "#" + input() + "#"
    print(line)
print("#" * (W + 2))