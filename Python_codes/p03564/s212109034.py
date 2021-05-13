N = int(input())
K = int(input())

ans = []
for i in range(1<<N):
    res = 1
    for j in range(N):
        if (1 & (i >> j)):
            res = res*2
        else:
            res = res + K
    ans.append(res)

print(min(ans))
