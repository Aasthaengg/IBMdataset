
A,B = map(int,input().split())
#%%
H,W = 100,100
S = [[0]*H for _ in range(W)]
f = True
if A>B:
    A,B = B,A
    f = False
def change(r,c,state):
    for i in range(r,r+3):
        for j in range(c,c+3):
            S[i][j] = 1
    
    if state==0:
        S[r+1][c+1] = 0    
        return
    elif state==1:
        S[r+1][c+1] = 0
        for i in range(3):
            S[r+3][c+i] = 1
            S[r+i][c+3] = 1
        S[r+3][c+3] = 1
        if c+4==W:
            for i in range(4):
                S[r+i][c+3] = 0
            
        return
    elif state==2:     
        return
    


r,c = 0,0
white = 1
black = 0
while white!=A or black!=B:
    if white<A and black<B-1:
        change(r,c,0)
        white += 1
        black += 1
        
    elif white<A:
        change(r,c,1)
        white += 1
        
    elif black<B:
        change(r,c,2)
        black += 1
        
    else:
        break
    if c+4==W:
        c = 0
        r += 4
    else:
        c += 4

if f:
    T = [['.']*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j]==1:
                T[i][j]='#'
else:
    T = [['#']*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j]==1:
                T[i][j]='.'
print(H,W)
for t in T:
    print(''.join(t))