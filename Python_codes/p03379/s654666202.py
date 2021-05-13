N=int(input())
X=list(map(int,input().split()))
Z=sorted(X)
left=Z[N//2-1]
right=Z[N//2]
for i in X:
    if i<=left:
        print(right)
    else:
        print(left)