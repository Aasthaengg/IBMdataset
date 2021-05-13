from _collections import defaultdict
n=int(input())
S=input()
X=defaultdict(int)
for s in S:
    X[s]+=1
ans=1
for v in X.values():
    ans*=(v+1)
print((ans-1)%(10**9+7))