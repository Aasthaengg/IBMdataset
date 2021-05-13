H,W = map(int,input().split())
S = []
S.append('.'*(2+W))
for i in range(H):
    S.append('.'+input()+'.')
S.append('.'*(2+W))
Sans = []
for i in range(1,H+1):
    S1 = ''
    for j in range(1,W+1):
        ans = 0
        if S[i][j] == '.':
            if S[i-1][j-1] == '#':
                ans +=1
            if S[i-1][j] == '#':
                ans +=1
            if S[i-1][j+1] == '#':
                ans +=1
            if S[i][j-1] == '#':
                ans +=1
            if S[i][j+1] == '#':
                ans +=1
            if S[i+1][j-1] == '#':
                ans +=1
            if S[i+1][j] == '#':
                ans +=1
            if S[i+1][j+1] == '#':
                ans +=1
        if S[i][j] == '#':
            ans = '#'
        S1 += str(ans)
    Sans.append(S1)

for i in range(H):
    print(Sans[i])
