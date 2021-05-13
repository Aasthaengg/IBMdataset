r = [0]*4

for i in range(3):
    a,b = map(int,input().split())
    r[a-1]+=1
    r[b-1]+=1
if r.count(2) == 2 and r.count(1) == 2:
    print('YES')
else:
    print('NO')