H,W=map(int,input().split())
S=[list(input()+'.') for i in range(H)]
S.append(['.']*(W+1))
a=[[0]*W for i in range(H)]
for y in range(H):
    for x in range(W):
        if S[y][x]=='.':
            a[y][x]=len([1 for i in range(-1,2) for j in range(-1,2) if S[i+y][j+x]=='#'])
        else: a[y][x]='#'
for i in a:print(''.join(list(map(str,i))))