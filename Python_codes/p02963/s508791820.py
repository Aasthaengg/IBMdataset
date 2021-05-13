#S=10^9y3-x3
S=int(input())
X1=0
Y1=0

X2=10**9
Y2=1

X3=S%X2
Y3=S//X2

#小さい数字で確認しておこう
if X3!=0:
    Y3+=1
    X3=X2-X3

#print(X2*Y3-Y2*X3)
print(X1,Y1,X2,Y2,X3,Y3)