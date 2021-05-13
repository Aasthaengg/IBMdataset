n=int(input())
X=list(map(int,input().split()))
X_sort=sorted(X)
for i in range(n):
    a=X_sort[n//2-1]
    b=X_sort[n//2]
    if X[i]<=a:
        print(b)
    else:
        print(a)