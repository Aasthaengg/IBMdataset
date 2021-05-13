from collections import Counter


n = int(input())
v = list(map(int, input().split()))
a = Counter(v[::2]).most_common()
b = Counter(v[1::2]).most_common()

ans = 0
l = n//2
if a[0][0] != b[0][0]:
    ans = l - a[0][1] + l - b[0][1]
else:
    if len(b) > 1:
        x = l - a[0][1] + l - b[1][1]
        y = l - a[1][1] + l - b[0][1]

    else:
        x = l - a[0][1] + l
        y = l - b[0][1] + l

    ans = min(x, y)

print(ans)
