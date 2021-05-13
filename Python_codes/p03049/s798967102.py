N = int(input())
ans = 0
da =0
db = 0
dba = 0
for i in range(N):
    s = input()
    k = s.count('AB')
    ans += k
    if s[0] == 'B' and s[-1] == 'A':
        dba +=1
        continue
    if s[0] == 'B':
        db +=1
    if s[-1] == 'A':
        da +=1
if dba != 0:
    ans += dba -1
    if da >= 1:
        ans +=1
        da -=1
    if db >=1:
        ans +=1
        db -=1
    ans += min(da,db)
    print(ans)
    exit()
if dba == 0:
    ans += min(da,db)
    print(ans)
    exit()