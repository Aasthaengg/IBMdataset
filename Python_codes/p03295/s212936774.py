import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pairs = []
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    pairs.append((a, b))

pairs.sort(key=lambda x: x[1])  # 右端の値でソート
current_right = 0
ans = 0
for (l, r) in pairs:
    if l >= current_right:
        current_right = r
        ans += 1
print(ans)
