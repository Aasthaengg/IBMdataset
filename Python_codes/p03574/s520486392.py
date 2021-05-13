
H,W = map(int,input().split())
S = [list(input()) for i in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            continue
        else:
            count = 0
            for k in range(-1,2,1):
                for l in range(-1,2,1):
                    if j+k<0 or i+l<0 or j+k>=W or i+l>=H:
                        continue
                    if S[i+l][j+k]=="#":
                        count+=1
            S[i][j]=str(count)

for i in range(H):
    print("".join(S[i]))
