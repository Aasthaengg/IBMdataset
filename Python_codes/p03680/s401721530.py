N = int(input())
S = [int(input()) for _ in range(N)]
#print(S)

s = ()
nex = 1

for i in range(N):
    #print(S[nex-1])
    nex = S[nex-1]
    if nex == 2:
        print(i+1)
        break
    if i == N-1:
        print(-1)