import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

X = int(input())

costs = [105, 104, 103, 102, 101, 100]
for x in range(X):
    if 100 * x <= X <= 105 * x:
        print(1)
        quit()
print(0)