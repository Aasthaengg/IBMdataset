N = int(input())
S = []
for i in range(N):
    s,p = input().split()
    S.append([s,int(p),i+1])
S.sort( key = lambda S: (S[0],-S[1]))
for i in range(N):
    print(S[i][2])
