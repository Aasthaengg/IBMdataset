N, K = map(int, input().split())
ans = 1
for i in range(N):
    ans *= K if i == 0 else K - 1

print(ans)
