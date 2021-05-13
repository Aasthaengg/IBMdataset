n,m,x,y = map(int,input().split())
xl = list(map(int,input().split()))
yl = list(map(int,input().split()))
xl.append(x)
yl.append(y)
xl.sort()
yl.sort()

if xl[-1] < yl[0]:
    print('No War')
else:
    print('War')