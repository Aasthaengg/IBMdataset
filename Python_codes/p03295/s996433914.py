import sys
input = sys.stdin.readline
n, m = map(int, input().split())
conflict = []
for _ in range(m):
    a, b = map(int, input().split())
    conflict.append((a, b))
conflict.sort(key=lambda x: x[1])


ans = 0
X = 0
for L, R in conflict:
    if L <= X:
        continue
    X = R-1
    ans += 1
print(ans)
