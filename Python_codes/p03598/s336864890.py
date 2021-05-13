N = int(input())
K = int(input())
X = list(map(int, input().split()))

ans = 0
for i in range(N):
    if X[i] < K/2:
        ans += X[i]*2
    else:
        ans += (K-X[i])*2

print(ans)