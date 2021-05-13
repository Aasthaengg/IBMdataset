from collections import Counter

n = int(input())
d = Counter(list(map(int, input().split())))
ans = 0
for x, y in d.items():
    if x > y:
        ans += y
    else:
        ans += y-x
print(ans)

