from collections import Counter

n = int(input())
s = input()

cnt = Counter(s)

ans = 1

for v in cnt.values():
    ans *= v + 1
    ans %= (10 ** 9 + 7)

print(ans - 1)
