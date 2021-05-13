S = input()
N = len(S)
down = 0
up = 0
ans = 0
uA = [0]*(N+1)
dA = [0]*(N+1)
for i in range(N+1):
    uA[i] = up
    if i < N:
        if S[i] == "<":
            up += 1
        else:
            up = 0
for i in range(N, -1, -1):
    dA[i] = down
    if i > 0:
        if S[i-1] == ">":
            down += 1
        else:
            down = 0
for i in range(N+1):
    ans += max(uA[i], dA[i])
print(ans)