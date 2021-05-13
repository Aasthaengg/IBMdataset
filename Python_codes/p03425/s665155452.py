from itertools import combinations

n = int(input())
c = {
    "M": 0,
    "A": 0,
    "R": 0,
    "C": 0,
    "H": 0
}
ck = list(c.keys())
cnt = 0

for i in range(n):
    s = input()
    if s[0] in c.keys():
        c[s[0]] += 1
        cnt += 1

if cnt >= 3:
    ans = 0
    for p in list(combinations("MARCH", 3)):
        ans += c[p[0]] * c[p[1]] * c[p[2]]
    print(ans)
else:
    print(0)
