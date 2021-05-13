N,C,K = map(int,input().split())
T = []
for i in range(N):
    T.append(int(input()))

T.sort()

ans = 0
p = C
d_time = 0

for i in range(N):
    if T[i] - d_time > K or p == C:
        ans += 1
        d_time = T[i]
        p = 1
    else:
        p += 1

print(ans)
