import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

A, B, C, X = map(int, read().decode("utf-8").split())

ans = 0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            sum_ = a * 500 + b * 100 + c * 50
            if sum_ == X:
                ans += 1
print(ans)