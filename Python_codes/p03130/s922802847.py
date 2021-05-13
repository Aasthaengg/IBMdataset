l=[list(map(int, input().split())) for i in range(3)]
r=[0,0,0,0]
for i in range(3):
    r[l[i][0]-1]+=1
    r[l[i][1]-1]+=1
r.sort()
if r==[1,1,2,2]:
    print('YES')
else:
    print('NO')