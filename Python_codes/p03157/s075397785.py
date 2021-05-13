from collections import deque

H,W=map(int,input().split())

S=[]
for i in range(H):
    S.append([c=='#' for c in input()]) # 黒をTrueとする
# print(S)

a=[[[] for j in range(W)] for i in range(H)]
for i in range(H):
    for j in range(W):
        if 0<i and (S[i][j] ^ S[i-1][j]):
            a[i][j].append((i-1,j))
        if i<H-1 and (S[i][j] ^ S[i+1][j]):
            a[i][j].append((i+1,j))
        if 0<j and (S[i][j] ^ S[i][j-1]):
            a[i][j].append((i,j-1))
        if j<W-1 and (S[i][j] ^ S[i][j+1]):
            a[i][j].append((i,j+1))
'''
for ai in a:
    print(ai)
'''
ans=0
q=deque()
r=[[False for j in range(W)] for i in range(H)]
for i in range(H):
    for j in range(W):
        if not r[i][j]:
            b,w=0,0
            q.append((i,j));r[i][j]=True
            if S[i][j]:
                b+=1
            else:
                w+=1
            while q:
                ui,uj=q.popleft()
                for v in a[ui][uj]:
                    vi,vj=v
                    if not r[vi][vj]:
                        q.append((vi,vj));r[vi][vj]=True
                        if S[vi][vj]:
                            b+=1
                        else:
                            w+=1
            ans+=b*w
print(ans)