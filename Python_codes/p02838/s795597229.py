mod = 10**9 + 7
n = int(input())
a = list(map(int, input().split()))
keta = [[0,0] for _ in range(60)]
for i in a:
    for j in range(60):
        if (i >> j) & 1:
            keta[j][1] += 1
        else:
            keta[j][0] += 1
ans = 0
for i in range(len(keta)):
    lis = keta[i]
    ans += lis[0] * lis[1] * pow(2, i, mod)
    ans %= mod
print(ans)