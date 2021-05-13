n = int(input())
h = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += h[i]
    tmp = h[i]
    for j in range(i, n):
        if h[j] >= tmp:
            h[j] -= tmp
        else:
            tmp = h[j]
            h[j] = 0
print(ans)