n = int(input())
a = list(map(int,input().split()))
a.sort()
aminus = []
aplus = []
p = 0
q = 0
for i in a:
    if i >= 0:
        aplus.append(i)
        p += 1
    elif i < 0:
        aminus.append(i)
        q += 1
ans = []
cou = 0
if aplus and aminus:
    now = aminus[0]
    for i in range(p-1):
        ans.append((now,aplus[i]))
        now = now - aplus[i]
    aminus[0] = now
    now = aplus[p-1]
    for i in range(q):
        ans.append((now,aminus[i]))
        now = now - aminus[i]
    cou = now
elif aplus:
    now = aplus[0]
    for i in range(1,p-1):
        ans.append((now,aplus[i]))
        now = now - aplus[i]
    ans.append((aplus[p-1],now))
    cou = aplus[p-1] - now
elif aminus:
    now = aminus[q-1]
    for i in range(q-1):
        ans.append((now,aminus[i]))
        now = now - aminus[i]
    cou = now

print(cou)
for i in range(n-1):
    print(*ans[i])
