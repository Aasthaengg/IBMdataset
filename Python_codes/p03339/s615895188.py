N = int(input())
S = list(input())
E = [0]*N #i番目より左側に、右向いてる人が何人
W = [0]*N #i番目より右側に、左向いてる人が何人

for i in range(1,N):
    E[i] = E[i-1]
    if S[i-1]=="E":
        E[i]+=1
for i in range(1,N):
    W[N-i-1] = W[N-i]
    if S[N-i]=="W":
        W[N-i-1]+=1

out = [0]*N
for i in range(N):
    out[i] = (N-1) - (W[i]+E[i])
print(min(out))