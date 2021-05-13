N,K=map(int,input().split())

S=list(input())

eng=["a","b","c"]
ENG=["A","B","C"]

x=ENG.index(S[K-1])
S[K-1]=eng[x]

s=""
for i in range(len(S)):
    s+=S[i]
print(s)
