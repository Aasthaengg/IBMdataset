N, M = map(int, input().split())
S = [-1]*N
for i in range(M):
    s,c = map(int, input().split())
    if S[s-1] == c:
        continue
    elif S[s-1] == -1:
        S[s-1] = c
    else:
        print(-1)
        exit()

if S[0] == 0:
    if N != 1:
        print(-1)
        exit()
if S[0] == -1:
    if N != 1:
        S[0] = 1
    else:
        S[0] = 0

for i in range(N):
    if S[i] == -1:
        S[i] = 0

print(*S,sep="")

