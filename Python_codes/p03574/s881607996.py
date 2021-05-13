H,W=map(int,input().split())
S=[]
for i in range(H):
    S.append(list(input()))
for i in range(len(S)):
    for j in range(len(S[i])):
        a=0
        if S[i][j]=='.':
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    if (0<=k and k<=len(S)-1) and (0<=l and l<=len(S[i])-1) and S[k][l]=='#':
                        a+=1
            S[i][j]=str(a)
for i in range(len(S)):
    print(''.join(S[i]))