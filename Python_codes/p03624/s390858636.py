s=str(input())
X="abcdefghijklmnopqrstuvwxyz"
Y=[]
for i in range(len(X)):
    Y.append(X[i])
for i in range(len(X)):
    if X[i] in s:
        Y.remove(X[i])


if len(Y)==0:
    print("None")

else:
    print(Y[0])
        
