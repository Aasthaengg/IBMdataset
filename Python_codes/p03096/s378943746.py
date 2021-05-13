N = int(input())
C = [-1]

for _ in range(N):
    c = int(input())
    if c == C[-1]:
        continue
    else:
        C.append(c)

MOD = 10**9+7
dp = 1
prev = [0]*(max(C)+1)

for c in C[1:]:
    dp = (dp+prev[c]) % MOD
    prev[c] = dp
print(dp)
