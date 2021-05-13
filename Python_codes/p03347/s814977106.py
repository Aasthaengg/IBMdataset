N = int(input())
X = [int(input()) for _ in range(N)]
if X[0]:
    print(-1)
    exit()

ans = 0
for i in range(1, N):
    if X[i] == X[i-1] + 1:
        ans += 1
    elif X[i] > X[i-1] + 1:
        print(-1)
        exit()
    else:
        ans += X[i]
print(ans)