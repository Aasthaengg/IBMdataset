H,W=map(int,input().split())
S=["*"*(W+2)]
for _ in range(H):
    S.append("*"+input()+"*")
S.append("*"*(W+2))

T=[]

for y in range(H+2):
    H=""
    for x in range(W+2):
        if S[y][x]==".":
            K=0
            for b in range(-1,2):
                for a in range(-1,2):
                    K+=(S[y+b][x+a]=="#")
            H+=str(K)
        else:
            H+=S[y][x]
    T.append(H)

print("\n".join(map(lambda x:x[1:-1],T[1:-1])))
