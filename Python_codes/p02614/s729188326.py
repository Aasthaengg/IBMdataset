import copy
H,W,K=input().split()
H=int(H)
W=int(W)
K=int(K)
C= [list(input()) for i in range(H)]
counter=0
for j in range(1<<H+W):
    D=copy.deepcopy(C)
    for k in range(H+W):
        mask=1<<k
        if j&mask!=0:
            if k<W:
                for l in range(H):
                    D[l][k]='R'
            else:
                for m in range(W):
                    D[k-W][m]='R'
    black=sum(D,[]).count('#')
    if black==K:
        counter+=1
print(counter)