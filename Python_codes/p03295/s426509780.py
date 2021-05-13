N, M = map(int,input().split())
B = sorted([list(map(int,input().split())) for k in range(M)],key = lambda x: x[1])
now = -1
ans = 0
for e in B:
    if now <= e[0]:
        ans += 1
        now = e[1]
print(ans)
