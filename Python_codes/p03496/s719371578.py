n = int(input())
aa = list(map(int, input().split()))

mx_v = 0
mn_v = 0

for i in range(n):
    if aa[i] > mx_v:
        mx_v = aa[i]
        mx_i = i + 1
    if aa[i] < mn_v:
        mn_v = aa[i]
        mn_i = i + 1

ans = []

if abs(mx_v) >= abs(mn_v) and mx_v != 0:
    for i in range(n):
        if aa[i] < 0:
            ans.append((mx_i, i + 1))
    for i in range(1, n):
        ans.append((i, i + 1))

if abs(mx_v) < abs(mn_v):
    for i in range(n):
        if aa[i] > 0:
            ans.append((mn_i, i + 1))
    for i in range(n, 1, -1):
        ans.append((i, i - 1))

print(len(ans))
for x, y in ans:
    print(x, y)