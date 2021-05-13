import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
a = list(map(int, input().split()))
to = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    to[i] = a[i - 1]
ans = 0
for i in range(1, n + 1):
    if to[to[i]] == i:
        ans += 1
print(ans // 2)
