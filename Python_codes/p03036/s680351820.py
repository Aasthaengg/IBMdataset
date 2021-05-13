
r,d,x2000 = map(int,input().split())
X = [x2000]

for i in range(10):
    X.append(r*X[i]-d)

for i in range(1,len(X)):
    print(X[i])

