r,d,x = list(map(int,input().split()))
X = [0]*11
X[0] = x
for i in range(10):
    X[i+1] = r*X[i] - d
    print(X[i+1])