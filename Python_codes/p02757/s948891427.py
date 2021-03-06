n, p = map(int, input().split())
s = list(map(int, list(input())))

ans = 0

if p == 2:
    for i in range(n):
        if s[i] % 2 == 0:
            ans += i + 1
    print(ans)
    exit()

if p == 5:
    for i in range(n):
        if s[i] == 0 or s[i] == 5:
            ans += i + 1
    print(ans)
    exit()

num = 1
l = [0]
for i in range(n-1, -1, -1):
    l.append((num * s[i] + l[-1]) % p)
    num *= 10
    num %= p

from collections import Counter

dic = Counter(l)
for i in dic.values():
    ans += i * (i - 1) // 2

print(ans)