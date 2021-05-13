from collections import Counter


n = int(input())
v = list(map(int, input().split()))
a = Counter(v[::2]).most_common()
b = Counter(v[1::2]).most_common()

ans = 0

if a[0][1] > b[0][1]:
    ans += (n//2) - a[0][1]
    if a[0][0] == b[0][0]:
        if len(b) > 1:
            ans += (n//2) - b[1][1]
        else:
            ans += (n//2)
    else:
        ans += (n // 2) - b[0][1]
elif a[0][1] < b[0][1]:
    ans += (n // 2) - b[0][1]
    if a[0][0] == b[0][0]:
        if len(a) > 1:
            ans += (n // 2) - a[1][1]
        else:
            ans += (n // 2)
    else:
        ans += (n // 2) - a[0][1]
else:
    ans += (n // 2) - b[0][1]
    if a[0][0] == b[0][0]:
        if len(a) > 1:
            ans += (n // 2) - max(a[1][1], b[1][1])
        else:
            ans += (n // 2)
    else:
        ans += (n // 2) - a[0][1]

print(ans)
