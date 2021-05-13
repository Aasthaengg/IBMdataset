N, M = map(int, input().split())
c = []
ans = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    c.extend(tmp[1:])
cnt = [0 for i in range(M)]
for i in range(len(c)):
    tmp2 = c[i]-1
    cnt[tmp2] += 1

for i in range(M):
    if cnt[i] == N:
        ans += 1

print(ans)