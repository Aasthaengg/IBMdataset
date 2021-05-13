N = int(input())
S = input()
Black = [0]*(N+1)
White = [S.count('.')]*(N+1)
DispS = [S.count('.')]*(N+1)
for TN in range(0,N):
    Black[TN+1] = Black[TN]+[0,1][S[TN]=='#']
    White[TN+1] = White[TN]-[0,1][S[TN]=='.']
    DispS[TN+1] = Black[TN+1]+White[TN+1]
print(min(DispS))