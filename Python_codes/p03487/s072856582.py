from collections import Counter

n = int(input())
a = list(map(int, input().split()))

dic = Counter(a)

ans = 0

for i, j in dic.items():
    if i < j:
        ans += j-i
    if i > j:
        ans += j

print(ans)