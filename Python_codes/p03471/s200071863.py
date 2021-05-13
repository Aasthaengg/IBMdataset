N,Y=map(int,input().split())
t,T,M=1000,10**6,range(N+1)
A=[(T*T*i+T*j+(N-i-j)) for i in M for j in M if (9*i+4*j+N==Y//t)*(i+j<=N)>0]
if A:
    a,b=A[0]%T,A[0]//T
    b,c=b%T,b//T
else:
    a,b,c=-1,-1,-1
print(c,b,a)