mod = 10**9+7
N = int(input())
Ca = [int(input())-1 for i in range(N)]
C = []
p = -1
for c in Ca:
    if p != c:
        C.append(c)
    p = c
#print(C)
N = len(C)
if N<=2:
    print(1)
    exit()
L = [-1]*(2*10**5)
dp = [0]*N
dp[0] = 1
L[C[0]] = 0


for i, c in enumerate(C[1:], 1):
    if L[c] == -1:
        L[c] = i
        dp[i] = dp[i-1]
        continue
    else:
        dp[i] = (dp[i-1] + dp[L[c]]) % mod
        L[c] = i
print(dp[-1])

