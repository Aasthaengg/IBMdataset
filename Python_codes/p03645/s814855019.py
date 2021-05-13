N,M = list(map(int,input().split()))
xfrom1 = []
xton =[]
for i in range(M):
    a,b = list(map(int,input().split()))
    if a == 1:
        xfrom1.append(b)
    elif a== N:
        xton.append(b)
    elif b==N:
        xton.append(a)
if len(set(xfrom1) & set(xton)) >0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
    
