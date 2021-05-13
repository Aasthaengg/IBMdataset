from collections import Counter
n = int(input())
d = Counter(list(map(int, input().split())))
key = list(d.keys())

ans = 0
for k in key:
    if k > d[k]:
        ans += d[k]
    elif k == d[k]:
        pass
    else:
        ans += d[k] - k
print(ans)