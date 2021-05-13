MOD = 10**9+7
N,  M = map(int, input().split())
a = set()
for i in range(M):
    a.add(int(input()))
stair = [0 for _ in range(N+1)]
stair[0] = 1
if 1 not in a:
    stair[1] = 1

for i in range(2, N+1):
    if i in a:
        stair[i] = 0
    else:
        stair[i] = (stair[i-1] + stair[i-2]) % MOD
print(stair[N])