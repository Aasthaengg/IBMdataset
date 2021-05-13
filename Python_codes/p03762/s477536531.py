n,m=map(int,input().split())

x=list(map(int,input().split()))
y=list(map(int,input().split()))

X=[]
for i in range(1,len(x)):
    X.append(x[i]-x[i-1])
    
Y=[]
for j in range(1,len(y)):
    Y.append(y[j]-y[j-1])

A=len(X)
for a in range(int((len(X)+1)/2)):
    X[a]*=A
    if X[a]==X[len(X)-1-a]:
        pass
    else:
        X[len(X)-1-a]*=A
    A=A+len(X)-2*(a+1)
    
SX=sum(X)

B=len(Y)
for b in range(int((len(Y)+1)/2)):
    Y[b]*=B
    if Y[b]==Y[len(Y)-1-b]:
        pass
    else:
        Y[len(Y)-1-b]*=B
    B=B+len(Y)-2*(b+1)
    
SY=sum(Y)

print((SX*SY)%(10**9+7))