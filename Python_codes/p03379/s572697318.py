N,*X=map(int,open(0).read().split())
M=sorted(X)[N//2-1:N//2+1]
for x in X:
    print(M[x<M[1]])