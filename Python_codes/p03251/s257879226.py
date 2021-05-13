n,m,x,y=map(int,input().split())
X=max(list(map(int,input().split())))
Y=min(list(map(int,input().split())))
for z in range(x+1,y+1):
    if X<z<=Y:
        print("No War")
        break
else:
    print("War")
