n = int(input())
la = [int(w) for w in input().split()]

cnt = [0]*9
for a in la:
    if a > 3200:
        a = 3200
    cnt[a // 400] += 1

mi = len([_ for _ in cnt[:8] if _ > 0])
ma = mi+cnt[8]

if mi == 0:
    mi = 1

print(mi, ma)
