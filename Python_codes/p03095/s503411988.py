from collections import Counter

n = int(input())
s = list(map(str, input().rstrip()))

c = Counter(s)

dp = 1
for x in c.values():
    dp = dp * (x + 1)

dp = (dp - 1) % (10 ** 9 + 7)

print(dp)