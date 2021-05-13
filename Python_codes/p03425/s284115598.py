from itertools import combinations

N=int(input())
P={"M","A","R","C","H"}
X={x:0 for x in P}

for _ in range(N):
    S=input()
    if S[0] in P:
        X[S[0]]+=1

K=0
for (a,b,c) in combinations(P,3):
    K+=X[a]*X[b]*X[c]
print(K)
