N = int(input())
S = str(input())
W=[0] * N
E=[0] * N

for i in range(1, N):
    if S[i-1] == "W":
        W[i]=W[i-1]+1
    else:
        W[i]=W[i-1]
for i in range(N-2, -1, -1):
    if S[i+1] == "E":
        E[i]=E[i+1]+1
    else:
        E[i]=E[i+1]

tmp=W[0]+E[0]
for i in range(1, N):
    if tmp > W[i]+E[i]:
        tmp = W[i]+E[i]

print(tmp)