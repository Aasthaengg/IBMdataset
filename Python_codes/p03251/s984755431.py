n,m,X,Y=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
max_x=max(x)
min_y=min(y)
for Z in range(X+1,Y+1):
    if max_x<Z<=min_y:
        print("No War")
        exit()
print("War")