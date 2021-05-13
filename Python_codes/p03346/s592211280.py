N = int(input())
P = [int(input()) for _ in range(N)]

S = [0 for _ in range(N+1)]

for i in range(N):
    if S[P[i]-1]!=0:
        S[P[i]] = S[P[i]-1]+1
    else:
        S[P[i]] = 1
    
print(N-max(S))