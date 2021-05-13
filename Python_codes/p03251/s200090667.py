n,m,X,Y=map(int,input().split())
x=max(X,max(map(int,input().split())))
y=min(Y,min(map(int,input().split())))
print(["War","No War"][x<y])