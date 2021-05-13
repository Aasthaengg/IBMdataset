n,m = map(int,input().split())
nm = [list(map(int,input().split())) for _ in range(m)]

cnt = [0] * n

for n,m in nm:
    cnt[n-1] += 1
    cnt[m-1] += 1

if all([i % 2 == 0 for i in cnt]):
    print('YES')
else:
    print('NO')
