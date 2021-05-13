x, y, z, K = map(int, input().split())
a = sorted(list(map(int, input().split())))[::-1]
b = sorted(list(map(int, input().split())))[::-1]
c = sorted(list(map(int, input().split())))[::-1]

ans = []
for i in range(x):
    for j in range(y):
        if (i + 1) * (j + 1) > K:
            break
        for k in range(z):
            if (i + 1) * (j + 1) * (k + 1) > K:
                break
            ans.append(a[i] + b[j] + c[k])
ans = sorted(ans)[::-1]
print(*ans[:K])
