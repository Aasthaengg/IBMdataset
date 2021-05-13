N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [0]*(N+1)
mods = {}
ans = 0

mods[0] = 1

for i in range(N):
    S[i+1] = A[i] + S[i]
    t = S[i+1]%M
    if t in mods:
        mods[t] += 1
    else:
        mods[t] = 1

for k, v in mods.items():
    ans += v*(v-1)//2

print(ans)