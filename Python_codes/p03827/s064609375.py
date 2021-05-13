import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N = int(input())
S = input()

ans = 0
x = 0
for s in S:
    if s == "I":
        x += 1
    else:
        x -= 1
    ans = max(ans, x)
print(ans)