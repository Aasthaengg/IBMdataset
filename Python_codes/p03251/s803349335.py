n,m,x,y = map(int,input().split())
xi = list(map(int,input().split()))
yi = list(map(int,input().split()))
flagx, flagy, flagz = 0, 0,0
z = 0
for i in range(x+1,y+1):
    for j in range(n):
        if i <= xi[j]:
            flagx = 1
            break
    for k in range(m):
        if i > yi[k]:
            flagy = 1
            break
    if flagx == 0 and flagy == 0:
        flagz =1
        break
    flagx, flagy = 0, 0
if flagz == 0:
    print('War')
else:
    print('No War')