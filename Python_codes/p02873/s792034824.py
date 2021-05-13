import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

S = input()

S = S.replace("><", ">,<").split(",")

ans = 0
for t in S:
    a = t.count(">")
    b = t.count("<")
    tmp = max(a, b) + sum(range(a)) + sum(range(b))
    ans += tmp
print(ans)