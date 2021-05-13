n=int(input())
M=[]
for i in range(n):
    x,y=map(int,input().split())
    M.append([x,y])
M.sort(key=lambda x:(x[0],x[1]))
X=[]
Y=[]
for i in range(n-1):
    for j in range(i+1,n):
        a=M[i][0]-M[j][0]
        b=M[i][1]-M[j][1]
        if not [a,b] in Y:
            Y.append([a,b])
            X.append(1)
        else:
            X[Y.index([a,b])]+=1
ans=n
for i in range(len(Y)):
    ans=min(ans,n-X[i])
print(ans)