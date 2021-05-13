n,m=map(int,input().split())
a=list(map(int,input().split()))

b=[0]
for i in range(n):
    b.append((b[i]+a[i])%m)
db = dict()
for sb in b:
    if sb not in db:
        db[sb] = 0
    db[sb] += 1

res = 0
for sdb in db.values():
    res += (sdb * (sdb-1)) // 2

print(res)