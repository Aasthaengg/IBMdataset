n,m,X,Y=map(int,input().split())
x=sorted(list(map(int,input().split())))
y=sorted(list(map(int,input().split())))
ans='War'
for i in range(X+1,Y+1):
    if x[-1]<i and y[0]>=i:
        ans='No War'
        break
print(ans) 
