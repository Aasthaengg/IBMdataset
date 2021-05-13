import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

H,W = MI()
S = [['.']*(W+2)]
for i in range(H):
    S.append(['.'] + LS2() + ['.'])
S.append(['.']*(W+2))

ANS = [[] for i in range(H+1)]
for i in range(1,H+1):
    for j in range(1,W+1):
        if S[i][j] == '#':
            ANS[i].append('#')
        else:
            ANS[i].append(str([S[i-1][j-1],S[i-1][j],S[i-1][j+1],S[i][j-1],S[i][j+1],S[i+1][j-1],S[i+1][j],S[i+1][j+1]].count('#')))

for i in range(1,H+1):
    print(''.join(ANS[i]))
