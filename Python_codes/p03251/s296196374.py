n,m,x,y=map(int,input().split())
x=sorted(list(map(int,input().split()))+[x])
y=sorted(list(map(int,input().split()))+[y])
if x[-1]<y[0]:
    print('No War')
else:
    print('War')