from itertools import product

S=input()
x,y=map(int,input().split())
L=[len(i) for i in S.split("T")]

X={L[0]}
Y={0}
for i in L[2::2]:
    X={j+k for j,k in product(X,[-i,i])}
for i in L[1::2]:
    Y={j+k for j,k in product(Y,[-i,i])}

if x in X and y in Y:
    print("Yes")
else:
    print("No")