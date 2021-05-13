N,A,B,C,D=map(int,input().split())
S="*"+input()

X=[0]*(N+1)
Y=[0]*(N+1)

for k in range(1,N+1):
    if S[k]=="#":
        X[k]=X[k-1]+1
    else:
        Y[k]=Y[k-1]+1

if max(X[A:max(C,D)+1])>=2:
    print("No")
else:
    if C<D:
        print("Yes")
    elif C>D:
        F=False
        for k in range(B,min(N,D+1)):
            F|=(S[k-1:k+2]=="...")

        if F:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
