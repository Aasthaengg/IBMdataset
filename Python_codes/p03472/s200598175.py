n, h = map(int,input().split())
a = []
b = []
for i in range(n):
    ca, cb = map(int,input().split())
    a.append(ca)
    b.append(cb)

amax = max(a)
b.sort(reverse=True)
cnt = 0
while h > 0:
    if b and b[0] > amax:
        h -= b.pop(0)
        cnt += 1
    else:
        cnt += h//amax
        h -= amax * (h//amax)
        if h > 0:
            h -= amax
            cnt += 1
print(cnt)
