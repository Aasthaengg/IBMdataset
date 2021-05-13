from collections import Counter

n = int(input())
a = map(int, input().split())

c = Counter(a)
r = 1 if n % 2 == 0 else 0
for k, v in c.items():
    if r == 0 and k == 0 and v == 1:
        continue
    if k != 0 and k % 2 == r and v == 2:
        continue
    print(0)
    break
else:
    print(2**(n//2) % (10**9+7))
