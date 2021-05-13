import copy




N,X=map(int,input().split())
S=input()
lenS=len(S)

RS=S[::-1]

goukei=0
G=[]
G.append(0)
Rgoukei=0
RG=[]
for i in range(1,lenS):
    if S[i]=="C":
        if S[i-1]=="A":
            goukei+=1
    G.append(goukei)


RG.append(0)
for i in range(1,lenS):
    if RS[i]=="A":
        if RS[i-1]=="C":
            Rgoukei+=1
    RG.append(Rgoukei)
RG.reverse()

#print(G)
#print(RG)

for i in range(X):
    A,B=map(int,input().split())
    print(goukei-G[A-1]-RG[B-1])
