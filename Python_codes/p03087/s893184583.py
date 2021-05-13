N,Q=map(int,input().split())
S="*"+input()

T=[0]*(N+1)
U=[0]*(N+1)
for i in range(1,N+1):
    if S[i-1]=="A" and S[i]=="C":
        T[i]=T[i-1]+1
        U[i]=1
    else:
        T[i]=T[i-1]

H=[0]*Q
for k in range(Q):
    X,Y=map(int,input().split())
    H[k]=T[Y]-T[X-1]-U[X]
print("\n".join(map(str,H)))
