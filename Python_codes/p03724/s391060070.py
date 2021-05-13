N,M = map(int, input().split())
cnt = [0] * (N + 1)
for _ in range(M):
    a,b = map(int, input().split())
    cnt[a] += 1
    cnt[b] += 1

flag = True if all(c % 2 == 0 for c in cnt) else False

if flag:
    print('YES')
else:
    print('NO')