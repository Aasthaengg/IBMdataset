A,B,C=map(int,input().split())
X=min(A,B,C)
Z=max(A,B,C)
Y=A+B+C-(X+Z)

if (X*Y*Z)%2==0:
    print(0)
else:
    print(X*Y)
