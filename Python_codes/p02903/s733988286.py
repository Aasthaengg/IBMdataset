def colchange(x):
    if x==1:
        return 0
    elif x==0:
        return 1
H,W,A,B=map(int,input().split())
table=[[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(0,A):
        table[i][j]=colchange(table[i][j])
for i in range(0,B):
    for j in range(W):
        table[i][j]=colchange(table[i][j])
#print(table)
for i in range(H):
    print(*table[i],sep="")
