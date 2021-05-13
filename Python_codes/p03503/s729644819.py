n = int(input())
f = [list(map(int,input().split())) for i in range(n)]
p = [list(map(int,input().split())) for i in range(n)]
ans = -float("inf")
for i in range(1,2**10):
    now = 0
    for j in range(n):
        cou = 0
        for k in range(10):
            if (i >> k & f[j][k]) == 1:
                cou += 1
        now += p[j][cou]
    ans = max(ans,now)
print(ans)
