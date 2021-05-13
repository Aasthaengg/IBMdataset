
import itertools

def countstrs(s):
    return [(k, len(list(g))) for k, g in itertools.groupby(s)]

n, k = map(int, input().split())
s = input()
c = countstrs(s)

total = [0] * (len(c) + 1)
cur = 0
for i in range(len(c)):
    cur += c[i][1]
    total[i+1] = cur


res = 0
l = 0
r = (2*k) + 0
while l < len(c):
    if c[l][0] == "0":
        rr = r
    else:
        rr = r+1
    if rr > len(c):
        rr = len(c)
    res = max(res, total[rr] - total[l])
    l += 1
    r += 1

print(res)