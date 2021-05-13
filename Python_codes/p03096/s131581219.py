from collections import Counter
MOD = pow(10,9)+7
N = int(input())
C = [int(input()) for i in range(N)]

DP = [1]*N
counter = Counter()
for i in range(N):
    c = C[i]
    if i==0:
        counter[c]+=1
    elif i==1:
        if c!=C[i-1]:
            counter[c]+=1
    else:
        DP[i] = DP[i-1]
        if c!=C[i-1]:
            DP[i]+=counter[c]
            counter[c]+=DP[i-1]
print(DP[N-1]%MOD)