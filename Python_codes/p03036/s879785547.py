r,d,x=map(int,input().split())
X=[x]
for i in range(10):
    X.append(r*X[i]-d)
    print(X[i+1])