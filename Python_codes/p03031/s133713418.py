N, M = map(int, input().split())
S = [list(map(int, input().split()))[1:] for _ in range(M)]
P = list(map(int, input().split()))
ans = 0
for i in range(1<<N):
    ok = True
    for j in range(M):
        cnt = 0
        for s in S[j]:
            if i&(1<<(s-1)):
                cnt += 1
        if cnt%2 != P[j]:
            ok = False
            break
    if ok:
        ans += 1
print(ans)
