def yakusu(n):
    m = 1
    re = []
    while m ** 2 < n:
        a, md = divmod(n, m)
        if md == 0:
            re.append(m)
            re.append(a)
        m += 1
    if m ** 2 == n:
        re.append(m)
    return re

n, k = map(int, input().split())
aa = list(map(int, input().split()))
yk = yakusu(sum(aa))
yk.sort(reverse=True)
for y in yk:
    rs = [a % y for a in aa if a % y]
    if not rs:
        print(y)
        exit()
    if len(rs)==1:continue
    rs.sort()
    l = 0
    sl = rs[0]
    r = len(rs) - 1
    sr = y - rs[r]
    while 1:
        if l + 1 == r:
            if sl == sr and sl <= k:
                print(y)
                exit()
            else:
                break
        if sl > sr:
            r -= 1
            sr += y - rs[r]
            if sr > k: break
        else:
            l += 1
            sl += rs[l]
            if sl > k: break
print(1)
