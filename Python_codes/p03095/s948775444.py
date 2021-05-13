from collections import defaultdict
n = int(input())
s = list(input())
cnt = defaultdict(int)
for c in s:
    cnt[c] += 1
ans = 1
for k, v in cnt.items():
    ans *= v + 1

print((ans - 1) % (10 ** 9 + 7))