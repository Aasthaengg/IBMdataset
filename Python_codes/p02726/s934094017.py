N, X, Y = list(map(int,input().split()))
X -= 1
Y -= 1
ans = [0 for _ in range(N)]
for i in range(N - 1):
    for j in range(i + 1, N):
        ind = min(j - i, abs(X - i) + 1 + abs(j - Y))
        ans[ind] += 1
for i in range(1, N):  print(ans[i])