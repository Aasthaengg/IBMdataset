n,c = map(int,input().split())
xv = [list(map(int,input().split())) for _ in range(n)]

l1 = 0
r1 = 0
l1_tmp = 0
l2_tmp = 0
r1_tmp = 0
r2_tmp = 0
now = 0
lil = []
lir = []
ll = []
lr = []

for x,v in xv:
    r1_tmp += v - (x - now)
    r2_tmp = r1_tmp - x
    r1 = max(r1, r1_tmp)
    lir.append(r2_tmp)
    lr.append(r1_tmp)
    now = x

xv = xv[::-1]
now = 0

for x,v in xv:
    x = c - x
    l1_tmp += v - (x - now)
    l2_tmp = l1_tmp - x
    l1 = max(l1, l1_tmp)
    lil.append(l2_tmp)
    ll.append(l1_tmp)
    now = x

max_idx = 0
lir = lir[::-1]
lir2 = []
lil2 = []
for i in range(n):
    lir2.append((lir[i], i))
for i in range(n):
    lil2.append((lil[i], n-i-1))

lir2.sort(reverse = True)
lil2.sort(reverse = True)

count = 0
ans = 0
for i in range(n-1):
    while lir2[count][1] <= i:
        count += 1
        if count > n:
            break
    ans = max(ans, ll[i]+lir2[count][0])

count = 0
for i in range(n-1):
    while lil2[count][1] <= i:
        count += 1
        if count > n:
            break
    ans = max(ans, lr[i]+lil2[count][0])

print(max(r1, l1, ans))
