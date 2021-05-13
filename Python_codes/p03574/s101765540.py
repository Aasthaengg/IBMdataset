H,W=map(int,input().split())
s=[input() for _ in range(H)]
S=[]
S.append(['.' for _ in range(W+2)])
for i in range(H):
    s[i]='.'+s[i]+'.'
    S.append(list(s[i]))
S.append(['.' for _ in range(W+2)])
for i in range(1,H+1):
    for j in range(1,W+1):
        cnt=0
        if S[i][j]=='.':
            for k in range(-1,2):
                for l in range(-1,2):
                    if S[i+k][j+l]=='#':
                        cnt+=1
            S[i][j]=str(cnt)
for i in range(1,H+1):
    print(''.join(S[i][1:W+1]))

