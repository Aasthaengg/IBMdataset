from collections import Counter

N=int(input())
S=input()

ans=0
X=Counter()
Y=Counter(S)
for c in S:
    Y[c]-=1
    if Y[c]==0:
        del X[c]
    else:
        X[c]+=1
    ans=max(ans,len(X))
       

print(ans)
