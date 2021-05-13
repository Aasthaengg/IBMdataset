from collections import Counter

n = int(input())
lis = list(map(int, input().split()))

c = Counter(lis)

ans = 0
for key , value in c.items():
    if key > value:
        ans += value
    elif key < value:
        ans += value - key

print(ans)
