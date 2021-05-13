N=int(input())
K=int(input())
X=int(input())
Y=int(input())

P=N-K

if P>0:
    print(P*Y+K*X)
else:
    print(N*X)