N, L = map(int, input().split())
l = []
idx = (10**6, -1)

for i in range(1, N + 1):
    l.append(L + i - 1)
    if abs(L + i - 1) < idx[0]:
        idx = (abs(L + i - 1), i)
ans = 0
for i in range(1, N + 1):
    if i != idx[1]:
        ans += l[i - 1]
print(ans)
