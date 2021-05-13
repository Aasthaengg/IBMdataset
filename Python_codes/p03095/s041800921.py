from collections import Counter
n = int(input())
d = Counter(list(input()))
val = d.values()
ans = 1
for i in val:
    ans *= (i + 1)
    ans %= 10**9 + 7
print(ans - 1)