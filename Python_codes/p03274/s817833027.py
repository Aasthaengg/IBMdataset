N,K=map(int,input().split())
X=list(map(int,input().split()))

M=float("inf")
for i in range(N-K+1):
    a,b=X[i],X[i+K-1]
    if 0<=a or b<=0:
        M=min(M,max(abs(a),abs(b)))
    else:
        c=min(abs(a),abs(b))
        M=min(M,abs(a)+abs(b)+abs(c))
print(M)