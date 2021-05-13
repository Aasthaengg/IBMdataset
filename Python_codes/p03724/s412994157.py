N, M = map(int, input().split())
cnt = [0] * (N+1)
for _ in range(M):
    ta,tb = map(int, input().split())
    cnt[ta] += 1
    cnt[tb] += 1
cond = 0
for i in range(1,N+1):
    if cnt[i] % 2 == 1:
        cond = 1
        break

if cond:
    print('NO')
else:
    print('YES')