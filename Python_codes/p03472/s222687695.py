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
bsum = 0
for i in range(n):
    if b[i] <= amax or bsum >= h:
        break
    else:
        bsum += b[i]
        cnt += 1
h -= bsum
if h > 0:
    cnt += h//amax
    h -= amax * (h//amax)
if h > 0:
    h -= amax
    cnt += 1
print(cnt)
