n = int(input())
a = list(map(int, input().split()))
a.sort()

k = []
max_a = a[-1]
max_half = max_a / 2
for i in range(n):
    if a[i] >= max_half:
        if i == 0:
            k.append(a[i])
            break
        k.append(a[i])
        k.append(a[i-1])
        break
ans = 0
if len(k) == 1:
    ans = k[0]
else:
    if abs(max_half - k[0]) < abs(max_half - k[1]):
        ans = k[0]
    else:
        ans = k[1]

print(max_a, ans)