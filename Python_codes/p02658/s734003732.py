N=int(input())
A=list(map(int,input().split()))
X=1
if 0 in A:
    print(0)
else:
    for idx in range(N):
        X=X*A[idx]
        if X >10**18:
            print(-1)
            break
    else:
        print(X)
