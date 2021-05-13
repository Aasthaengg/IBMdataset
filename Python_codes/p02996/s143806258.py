N=int(input())

X=[0]*N
for k in range(1,N+1):
    a,b=map(int,input().split())
    X[k-1]=(a,b)

X.sort(key=lambda x:x[1])

D=0
F=True
for (s,t) in X:
    D+=s
    F&=D<=t

if F:
    print("Yes")
else:
    print("No")

