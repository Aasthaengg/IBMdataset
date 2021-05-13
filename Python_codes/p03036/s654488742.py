r, D, x2000 = map(int, input().split())
ans = [x2000]

for i in range(10):
    ans.append(ans[i] * r - D)
    print(ans[i + 1])
