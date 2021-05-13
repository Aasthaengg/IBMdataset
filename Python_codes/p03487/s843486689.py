n = int(input())
a = list(map(int, input().split()))

from collections import Counter

dic = Counter(a)

ans = 0
for i, j in dic.items():
    if i <= j:
        ans += j - i
    else:
        ans += j

print(ans)