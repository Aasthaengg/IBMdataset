r,D,x=map(int,input().split())

X=[x]
for i in range(10):
    a = r*X[i]-D
    X.append(a)
    print(a)