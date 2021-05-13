n = int(input())
f = []
for _ in range(n):
    f.append(list(map(int, input().split())))
p = []
for _ in range(n):
    p.append(list(map(int, input().split())))

ans = -10**9
for i in range(1, 2**10):
    profit = 0
    for ff, pp in zip(f, p):
        cnt = 0
        for j in range(10):
            cnt += ((i>>j)&1)&ff[j]
        profit += pp[cnt]
    ans = max(ans, profit)
print(ans)