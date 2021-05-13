n = int(input())
arms = []  # [s, t]のリスト
for _ in range(n):
    x, l = map(int, input().split())
    arms.append([x-l, x+l])
ans = 0
pre_t = -1 * float('inf')
arms.sort(key=lambda arm: arm[1])
for i in range(n):
    s, t = arms[i]
    if s >= pre_t:
        ans += 1
        pre_t = t
print(ans)