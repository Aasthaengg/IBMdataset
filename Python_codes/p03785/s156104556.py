N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]

T.sort()
s = -(10**10)
cnt = 0
res = 0
for t in T:
    if s+K < t:
        res += 1
        s = t
        cnt = 0
    if cnt == C:
        res += 1
        s = t
        cnt = 0
    cnt += 1

print(res)