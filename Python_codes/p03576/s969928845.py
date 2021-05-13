n,K=map(int,input().split())
S=[[0 for i in range(n+1)] for j in range(n+1)]
p=[list(map(int,input().split())) for i in range(n)]
p.sort(key=lambda x:x[1])
for i in range(n):
    p[i].append(i)
p.sort()
y=[0]*n
for i in range(n):
    y[i]=p[i][2]
for i in range(n):
    S[i+1][y[i]+1]=1
X=[p[i][0] for i in range(n)]
Y=[p[i][1] for i in range(n)]
X.sort();Y.sort()
for i in range(1,n+1):
    for j in range(1,n+1):
        S[i][j]=S[i][j]+S[i][j-1]+S[i-1][j]-S[i-1][j-1]
ans=10**20
for i in range(n):
    for j in range(n):
        for k in range(i+1,n+1):
            for l in range(j+1,n+1):
                if S[k][l]-S[k][j]-S[i][l]+S[i][j]>=K:
                    #print(S[k][l]-S[k][j]-S[i][l]+S[i][j])
                    if ans > (X[k-1]-X[i])*(Y[l-1]-Y[j]):
                        ans = (X[k-1]-X[i])*(Y[l-1]-Y[j])
                #print(ans)
print(ans)