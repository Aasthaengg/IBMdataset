N = int(input())
ans = []
if N % 2 == 0:
    # 偶数のとき
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if i + j == N+1:
                continue
            ans.append((i, j))
else:
    # 奇数のとき
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if i + j == N:
                continue
            ans.append((i, j))

print(len(ans))
for s, t in ans:
    print(s, t)
