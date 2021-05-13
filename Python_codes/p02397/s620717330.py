x,y = map(int,input().split())

while not(x==0 and y==0):
    if x>y:
        x,y = y,x
    print('{0} {1}'.format(x,y))
    x,y = map(int,input().split())

