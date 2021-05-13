import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

n, *v = map(int, read().split())

v = sorted(v)
ans = v[0]

for i in range(1, n):
    ans = (ans + v[i]) / 2

print(ans)