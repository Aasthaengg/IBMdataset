from collections import Counter

As = input()

lenA = len(As)
cnt = Counter(As)

ans = lenA * (lenA - 1) // 2
for c, num in cnt.items():
    ans -= num * (num - 1) // 2
print(ans + 1)
