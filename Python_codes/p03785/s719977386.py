n, c, k, *t = map(int, open(0).read().split())
t.sort()
tmp = 0
cnt = 0
limit = t[0] + k
for time in t:
    if tmp == c or time > limit:
        limit = time + k
        tmp = 1
        cnt += 1
    else:
        tmp += 1
if tmp != 0:
    print(cnt + 1)
else:
    print(cnt)