import collections

n, *a = map(int, open(0).read().split())
c = collections.Counter(a)
length_l = list(c.keys())
length_l.sort(reverse = True)
side1 = 0
ans = 0
for l in length_l:
    cnt = c[l]
    if cnt >= 4:
        if side1 != 0:
            ans = side1*l
            break
        else:
            ans = l**2
            break
    elif cnt >= 2:
        if side1 != 0:
            ans = side1*l
            break
        else:
            side1 = l
print(ans)