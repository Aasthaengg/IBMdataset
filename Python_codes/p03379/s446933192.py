N = int(input())
X = list(map(int,input().split()))
Y = sorted(X)
big,small = Y[N//2],Y[N//2-1]
for i in X:
    if i <= small:
        print(big)
    else:
        print(small)