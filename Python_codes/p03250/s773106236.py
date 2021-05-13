A,B,C=map(int,input().split())

X=[A,B,C]

Y=sorted(X,reverse=True)

print(Y[0]*10+Y[1]+Y[2])