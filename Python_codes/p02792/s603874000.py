n = int(input())
lis = [[0 for i in range(10)] for j in range(10)]
for i in range(1, n+1):
    s = str(i)
    l = int(s[0])
    r = int(s[-1])
    lis[l][r] += 1
ans = 0
for i in range(10):
    for j in range(10):
        if i == j:
            ans += lis[i][j] ** 2
        else:
            ans += lis[i][j] * lis[j][i]
print(ans)