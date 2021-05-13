from collections import Counter
n = int(input())
a = [int(x) for x in input().split()]

c = Counter(a)
ans = 0
for x in c:
    if c[x] < x:
        ans += c[x]
    else:
        ans += c[x] - x

print(ans)