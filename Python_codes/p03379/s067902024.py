N = int(input())
X = list(map(int,input().split()))
copy_X = X.copy()
X.sort()
for i in copy_X:
    if(i<X[N//2]):
        print(X[N//2])
    else:
        print(X[(N//2)-1])