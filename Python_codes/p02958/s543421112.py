N, *P = map(int, open(0).read().split())

ans = 0
for i in zip(P, range(1,N+1)):
    if i[0] != i[1]:
        ans += 1

print('YES' if ans == 0 or ans == 2 else 'NO')