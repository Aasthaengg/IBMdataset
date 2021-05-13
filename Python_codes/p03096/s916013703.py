# B
N = int(input())
C_list = [0]*N
for i in range(N):
    C_list[i] = int(input()) - 1
    
LARGE = 10**9+7

T = 1
DP = [0]*(max(C_list) + 1)

for i in range(N):
    c = C_list[i]
    if i > 0:
        if C_list[i] == C_list[i-1]:
            pass
        else:
            T, DP[c] = (T + DP[c]) % LARGE, (DP[c] + T) % LARGE
    else:
        T, DP[c] = (T + DP[c]) % LARGE, (DP[c] + T) % LARGE
print(T)