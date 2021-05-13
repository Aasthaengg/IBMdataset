n,m = map(int,input().split())

#p = [-1]*m
#y = [-1]*m
ipy=[]

for i in range(m):
    ipy.append(list(map(int,(str(i) + " " + input()).split())))

ipy = sorted(ipy, key = lambda x: (x[1], x[2]))

ipy[0][2] = 1
for i in range(1,m):
    if ipy[i][1] == ipy[i-1][1]:
        ipy[i][2] = ipy[i-1][2]+1
    else:
        ipy[i][2] = 1

ipy = sorted(ipy, key = lambda x: x[0])

for i in range(m):
    print(f'{ipy[i][1]:06}'+f'{ipy[i][2]:06}')

