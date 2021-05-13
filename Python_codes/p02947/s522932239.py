import collections

n = int(input())
s = list(sorted(input()) for _ in range(n))

l = []
for li in s:
    st = ''
    for x in li:
        st += x
    l.append(st)

c = collections.Counter(l)

ans = 0
for x in c.values():
    ans += x * (x - 1) // 2

print(ans)
