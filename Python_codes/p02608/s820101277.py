N = int(input())

ans = [0 for _ in range(100001)]

for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 105):
            v = i*i + j*j + k*k + i*j + j*k + k*i
            if v < 10001:
                ans[v] += 1

for n in range(N):
    print(ans[n+1])
