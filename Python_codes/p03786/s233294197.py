def count(l):
    res = {}
    for d in l:
        if d in res:
            res[d] += 1
        else:
            res[d] = 1
    return res
n = int(input())
data = list(map(int, input().split()))
cnt = count(data)
monsters = sorted(cnt.keys())
total = sum(data)
ans = n
idx = len(monsters)-2
while idx >= 0:
    prev = monsters[idx+1]
    total -= prev*cnt[prev]
    if total*2 < prev:
        break
    idx -= 1
out = 0
while idx >= 0:
    m = monsters[idx]
    out += cnt[m]
    idx -= 1

ans -= out 
print(ans)