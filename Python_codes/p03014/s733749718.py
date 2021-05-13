H,W = map(int,input().split())
S = [list(input()) for i in range(0,H,1)]

teraseru_H = [[0 for i in range(0,W,1)]for j in range(0,H,1)]
teraseru_W = [[0 for i in range(0,W,1)]for j in range(0,H,1)]

left = -1
for i in range(0,H,1):
    left=-1
    for j in range(0,W,1):
        if S[i][j]=="#":
            if left!=-1:
                for k in range(left,j,1):
                    teraseru_H[i][k] = j-left
                left=-1

        else:#"."
            if left==-1:
                left=j
    if left!=-1:
        for k in range(left,W,1):
            teraseru_H[i][k] = W-left
    left=-1

left = -1
for j in range(0,W,1):
    left=-1
    for i in range(0,H,1):
        if S[i][j]=="#":
            if left!=-1:
                for k in range(left,i,1):
                    teraseru_W[k][j] = i-left
                left=-1
        else:#"."
            if left==-1:
                left=i
    if left!=-1:
        for k in range(left,H,1):
            teraseru_W[k][j] = H-left
    left=-1

ans = 0

for i in range(0,H,1):
    for j in range(0,W,1):
        ans = max(ans,teraseru_H[i][j]+teraseru_W[i][j]-1)
print(ans)