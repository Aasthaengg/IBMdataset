n,m,X,Y = map(int,input().split())
x = max(list(map(int,input().split())))
y = min(list(map(int,input().split())))
if y-x > 0 and x < Y and y > X:
    print('No War')
else:
    print('War')
