N = int(input())
S = input()

Ecnt = S.count('E')
Wcnt = S.count('W')

E = [0] * N
W = [0] * N

if S[0]=='E':
    E[0] = 1
else:
    W[0] = 1

for i in range(1, N):
    if S[i]=='E':
        E[i] = E[i-1] + 1
        W[i] = W[i-1]
    else:
        W[i] = W[i-1] + 1
        E[i] = E[i-1]
        
E = [0] + E
W = [0] + W
# print('E', E, 'W', W)

score=[]
for i in range(N):
        score.append(W[N]-W[i+1] + E[i]-E[0])
print(N-max(score)-1)