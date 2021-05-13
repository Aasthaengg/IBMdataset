N, C, K = map(int, input().split())
T = sorted([int(input()) for i in range(N)])

bs = 0
st = 0
ans = 0
for t in T:
    if bs == 0:
        st = t
    if bs == C or t-st>K:
        bs = 1
        st = t
        ans += 1
    else:
        bs += 1

if bs > 0:
    ans += 1
print(ans)
