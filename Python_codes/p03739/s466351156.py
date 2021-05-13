n = int(input())
a = list(map(int,input().split()))
acc = [a[0]]
for i in range(1, n):
    acc.append(acc[-1] + a[i])

res = 10 ** 100

def f(fir):
    prv_pos = fir > 0
    margin = fir - a[0]
    ret = abs(margin)
    for i in range(1, n):
        cur = margin + acc[i]
        if prv_pos and cur < 0:
            prv_pos = not prv_pos
            continue
        if not prv_pos and cur > 0:
            prv_pos = not prv_pos
            continue
        if prv_pos:
            need = -1
            sa = need - cur
            margin += sa
            ret += abs(sa)
        else:
            need = 1
            sa = need - cur
            margin += sa
            ret += abs(sa)
        prv_pos = not prv_pos
    return ret


res = min(res, f(1))
res = min(res, f(-1))
if a[0] != 0:
    res = min(res, f(a[0]))
print(res)
