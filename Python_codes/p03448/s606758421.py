X = [int(input()) for _ in range(4)]
ans = 0
for i in range(X[0] + 1):
    for j in range(X[1] + 1):
        for k in range(X[2] + 1):
            if 500 * i + 100 * j + 50 * k == X[3]:
                ans += 1
print(ans)