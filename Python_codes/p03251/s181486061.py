N,M,X,Y=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
z=[]
for i in range(X+1,Y+1):
    if max(x)<i and min(y)>=i:
        z.append(i)
if len(z)>=1:
    print('No War')
else:
    print('War')