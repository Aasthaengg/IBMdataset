N,M = map(int,input().split())
ls = []
for i in range(M):
    P,Y = map(int,input().split())
    ls.append([P,Y,i])
ls.sort()
num = 1
city = ls[0][0]
for i in range(M):
    if ls[i][0] == city:
        ls[i][1] = num
        num += 1
    else:
        num = 1
        ls[i][1] = num
        city = ls[i][0]
        num += 1
ls.sort(key=lambda x:x[2])
for i in range(M):
    print('{0:06d}'.format(ls[i][0])+'{0:06d}'.format(ls[i][1]))