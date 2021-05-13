N,K=map(int,input().split())
X=list(map(int,input().split()))
answers=[]
whole=0
for n in range(N-K+1):
    if X[K-1+n]>0 and X[n]<0:
        whole += (X[K - 1 + n] - X[n])
        whole+=min(X[K-1+n],-X[n])
    elif X[K-1+n]<0:
        whole-=X[n]
    elif X[n]>0:
        whole+=X[K-1+n]
    answers.append(whole)
    whole=0
print(min(answers))
