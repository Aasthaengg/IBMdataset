n = int(input())

ans = [0] * (n+1)
for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            tmp = i*i + j*j + k*k + i*j + j*k + i*k
            if tmp <= n:
                ans[tmp] += 1

for i in range(1, n+1):
    print(ans[i])
