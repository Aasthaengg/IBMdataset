import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

X = int(input())

ans = 1
for i in range(2, X):
    b = i
    p = 2
    a = b ** p
    while a <= X: 
        ans = max(ans, a)
        p += 1
        a = b ** p
print(ans)