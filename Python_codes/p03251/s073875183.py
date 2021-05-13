N,M,X,Y=map(int,input().split())
x=[int(x) for x in input().split()]
y=[int(x) for x in input().split()]
ans=False
for z in range(X+1,Y+1):
    if max(x)<z<=min(y):
        ans=True

if ans==True:
    print("No War")
else:
    print("War")
