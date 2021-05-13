r, d, x2000 = map(int, input().split())
ans = [0] * 10

ans[0] = r * x2000 - d
print(ans[0])

for i in range(1, 10):
    ans[i] = r * ans[i - 1] - d
    print(ans[i])