N, C, K = map(int, input().split())
t = []
for i in range(N):
    t.append(int(input()))
t.sort()

ans = 0
pt = t[0]
cnt = 1

for i, ct in enumerate(t[1:]):
    if ct - pt > K:
        ans += 1
        cnt = 1
        pt = ct
    elif ct - pt <= K and cnt <= C:
        if cnt == C:
            ans += 1
            cnt = 0
            pt = ct
        cnt += 1
        
if cnt > 0:
    ans += 1
    
print(ans)