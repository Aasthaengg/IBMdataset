from collections import Counter
N = int(input())
a = [int(i) for i in input().split()]

ans = 0
m = Counter(a)
for x, y in m.items():
    if x == y:
        continue
    elif x < y:
        ans += abs(y-x)
    else:
        ans += y
print(ans)