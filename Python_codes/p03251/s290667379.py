n,m,x,y = map(int,input().split())
xi = list(map(int,input().split()))
xi.append(x)
yi=  list(map(int,input().split()))
yi.append(y)
if  max(xi)<min(yi):
    print('No War')
else:
    print('War')