from collections import Counter


n, p = map(int, input().split())
S = map(int, reversed(input()))

if p == 2 or p == 5:
    ans = 0
    mods = map(lambda x: x % p, S)
    for idx, mod in enumerate(mods):
        if mod == 0:
            ans += n - idx
    print(ans)
    exit()

mods = [0]
num = 0
digit = 1
for s in S:
    num += s * digit
    num %= p
    mods.append(num)
    digit = digit * 10 % p

counter = Counter(mods)
ans = 0
for count in counter.values():
    ans += count * (count-1) // 2
print(ans)
