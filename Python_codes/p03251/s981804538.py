n,m,x,y = map(int,input().split())
x_max = sorted(list(map(int,input().split())))[-1]
y_min = sorted(list(map(int,input().split())))[0]

if x<=x_max<y_min<=y:
    print('No War')
else:
    print('War')