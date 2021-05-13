N = int(input())
S = input()
#%%
cum = [[0]*(N+1) for _ in range(3)]
for i in range(N):
    cum[0][i+1] = cum[0][i] + (S[i]=='R')
    cum[1][i+1] = cum[1][i] + (S[i]=='G')
    cum[2][i+1] = cum[2][i] + (S[i]=='B')
    
def color(i,j):
    RGB = [0]*3
    if S[i]=='R' or S[j]=='R':
        RGB[0] = 1
    if S[i]=='G' or S[j]=='G':
        RGB[1] = 1
    if S[i]=='B' or S[j]=='B':
        RGB[2] = 1
    
    if RGB[0]==0:
        return 0
    elif RGB[1]==0:
        return 1
    else:
        return 2
def col(s):
    if s=='R':
        return 0
    elif s=='G':
        return 1
    else:
        return 2

ans = 0
for i in range(N):
    for j in range(i+1,N):
        if S[i]!=S[j]:
            idx = color(i,j)
            ans += cum[idx][N]-cum[idx][j+1]
            k = 2*j-i
            if k<N and col(S[k])==idx:
                ans -= 1
print(ans)
