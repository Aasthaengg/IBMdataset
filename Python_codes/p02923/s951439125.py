N = int(input())
H = list(map(int, input().split()))
DP = [0]*(N+1)
for i in range(N-1):
    if H[i+1] <= H[i]:
        DP[i+1] = DP[i]+1
print(max(DP))