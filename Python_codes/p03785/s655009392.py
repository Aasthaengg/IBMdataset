N, C, K = map(int, input().split())
T = []
for _ in range(N):
    T.append(int(input()))
T = sorted(T)

ans = 0
c = 0
s = 0

for t in T:
    if (s != 0) and (s + K < t):
        s = 0
        c = 0
        ans += 1

    if s == 0:
        s = t
    c += 1

    if c == C:
        s = 0
        c = 0
        ans += 1
    #print(t, s, c, ans)

if s != 0:
    ans += 1

print(ans)