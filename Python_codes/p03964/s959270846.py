
def func(n,x):
    if n%x!=0:
        return n+(x-n%x)
    else:
        return n
X=[]
n=int(input())
for i in range(n):
    t,a=map(int,input().split())
    X.append([t,a])

T=X[0][0]
A=X[0][1]

for i in range(1,n):
    if T<=X[i][0] and A<=X[i][1]:
        T=X[i][0]
        A=X[i][1]
    elif T>X[i][0] and A<=X[i][1]:
        T=func(T,X[i][0])
        A=T*X[i][1]//X[i][0]
    elif T<=X[i][0] and A>X[i][0]:
        A=func(A,X[i][1])
        T=A*X[i][0]//X[i][1]
    else:
        T=func(T,X[i][0])
        A=func(A,X[i][1])
        if T>A*X[i][0]//X[i][1]:
            A=T*X[i][1]//X[i][0]
        else:
            T=A*X[i][0]//X[i][1]
print(T+A)