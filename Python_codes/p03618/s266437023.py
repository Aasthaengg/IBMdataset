s = input()
n = len(s)

from collections import Counter
cnt = Counter(s)

ans = n * (n - 1) // 2 + 1
for _, x in cnt.items():
    ans -= x * (x - 1) // 2

print(ans)