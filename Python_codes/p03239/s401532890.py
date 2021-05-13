
[N,T] = list(map(int,input().split()))

ct = []
for i in range(N):
    ct.append(list(map(int,input().split())))

cost=[]
for i in range(N):
    if ct[i][1] <= T:
        cost.append(ct[i][0])

if len(cost)==0:
    print('TLE')
else:
    print(min(cost))