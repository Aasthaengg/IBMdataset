N=int(input())
S=input()
K=10**9+7

T={}
for s in S:
    if s in T:
        T[s]+=1
    else:
        T[s]=2

X=1
for a in T:
    X=(X*T[a])%K
print((X-1)%K)
