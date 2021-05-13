N,M,X,Y=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
for z in range(-100,101):
    if max(x)<z and z<=min(y) and X<z and z<=Y: print('No War');exit()
print('War')