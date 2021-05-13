from itertools import product

N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(N)]

ans = 10**10
for l in product([False, True], repeat=N):
    for i in range(M):
        if sum(ca[i+1] for j, ca in enumerate(CA) if l[j]) < X:
            break
    else:
        s = sum(ca[0] for j, ca in enumerate(CA) if l[j])
        ans = min(ans, s)
print(-1 if ans == 10**10 else ans)
