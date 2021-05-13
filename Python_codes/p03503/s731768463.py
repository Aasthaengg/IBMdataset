n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]
ans = -float("inf")
for i in range(1,2**10):
    res = 0
    for j in range(n):
        tnp = 0
        for k in range(10):
            if ((i>>k)&1):
                if (f[j][k]==1):
                    tnp += 1
        res += p[j][tnp]
    ans = max(ans,res)
print(ans)