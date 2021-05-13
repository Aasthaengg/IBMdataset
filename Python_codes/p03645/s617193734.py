n,m=map(int,input().split())
a=[]
for i in range(m):
    a.append(list(map(int,input().split())))
a.sort()
#print(a)
d=[]
for i in range(m):
    if a[i][0]==1:
        d.append(a[i][1])
    else:
        break
e=[]
for i in range(m):
    if a[i][1]==n:
        e.append(a[i][0])
if len(set(e) & set(d))!=0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')

