S = input()

pd = [[0]*2 for _ in range(len(S))]
if S[0] != S[1] :
    pd[1][0] = 1

for i in range(2,len(S)) :
    pd[i][0] = pd[i-1][1] + 1
    if S[i] != S[i-1] :
        pd[i][0] = max(pd[i][0], pd[i-1][0]+1)
    pd[i][1] = pd[i-2][0] + 1
    if S[i-1:i+1] != S[i-3:i-1] :
        pd[i][1] = max(pd[i][1], pd[i-2][1]+1)

print(max(pd[len(S)-1])+1)
