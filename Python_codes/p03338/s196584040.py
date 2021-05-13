import collections

N=int(input())
S=input()

ans=0
X=collections.Counter()
Y=collections.Counter(S)
for c in S:
    X[c]+=1
    Y[c]-=1
    ans=max(ans,len(X&Y))
       
print(ans)
