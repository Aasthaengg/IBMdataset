import bisect

s = input()
t = input()
p = {}
for i in range(len(s)):
    c = s[i]
    if c not in p:
        p[c] = []
    p[c].append(i)

over = 0
ret = 0
for c in t:
    if c not in p:
        print(-1)
        exit(0)
    ind = bisect.bisect_left(p[c], ret)
    if ind < len(p[c]):
        ret = p[c][ind] + 1
    else:
        ret = p[c][0] + 1
        over += 1

print(over * len(s) + ret)