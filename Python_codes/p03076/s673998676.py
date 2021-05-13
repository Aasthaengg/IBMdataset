import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

L = list(map(int, read().decode("utf-8").split()))

last_ = L[0] % 10
last_index = 0
for i, t in enumerate(L):
    if 0 < t % 10 < last_:
        last_ = t % 10
        last_index = i

ans = 0
for i, t in enumerate(L):
    if i != last_index:
        ans += t
        if t % 10:
            ans += 10 - (t % 10)
ans += L[last_index]
print(ans)