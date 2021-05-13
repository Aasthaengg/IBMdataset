from collections import Counter

n = int(input())
a = list(map(int, input().split()))

cnt = Counter(a)
ans = 0
for key, val in cnt.items():
    if val < key:
        ans += val
    else:
        ans += val - key

print(ans)
