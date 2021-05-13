X1,Y1,X2,Y2 = list(map(int,input().split()))

X3 = X2 + -1*(Y2-Y1)
Y3 = Y2 + (X2-X1)
X4 = X3 + -1*(Y3-Y2)
Y4 = Y3 + (X3-X2)
print(X3,Y3,X4,Y4)
