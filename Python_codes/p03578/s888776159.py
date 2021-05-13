n = int(input())
d = list(map(int,input().split()))
m = int(input())
t = list(map(int,input().split()))
if n < m:
    print('NO')
    exit(0)
dcnt = {}
for x in d:dcnt[x] = 0
ok = True
for x in d:dcnt[x]+=1
for i in range(m):
    if t[i] not in dcnt:
        ok = False
        break
    if dcnt[t[i]] == 0:
        ok = False
        break
    dcnt[t[i]] -= 1
if ok:print('YES')
else:print('NO')
