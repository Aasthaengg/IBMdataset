A,B,C=map(int,input().split())
P=A+B
R=A+C
Q=C+B
if Q>P:
  X=P
else:
    X=Q
if R>X:
    print(X)
else:print(R)