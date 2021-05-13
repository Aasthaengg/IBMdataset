N,T=map(int,input().split())
ct=[]
d=[]
for i in range(N):
    ct.append(list(map(int,input().split())))
for i in range(N):
    if ct[i][1]<=T:
        d.append(ct[i])
if len(d)==0:
    print('TLE')
else:
    e=d[0]
    for i in range(len(d)):
        if e[0]>=d[i][0]:
            e=d[i]
    print(e[0])