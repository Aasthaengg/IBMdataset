H,W=map(int,input().split())
s=[input() for _ in range(H)]
S=[]
S.append(['.' for _ in range(W+2)])
for i in range(H):
    s[i]='.'+s[i]+'.'
    S.append(list(s[i]))
S.append(['.' for _ in range(W+2)])
ans=True
for i in range(1,H+1):
    for j in range(1,W+1):
        if S[i][j]=='#':
            flag=False
            for k in range(-1,2,2):
                if S[i+k][j]=='#' or S[i][j+k]=='#':
                    flag=True
                    break
            if flag==False:
                ans=False
                break
    else:
        continue
    break
if ans:
    print("Yes")
else:
    print("No")            