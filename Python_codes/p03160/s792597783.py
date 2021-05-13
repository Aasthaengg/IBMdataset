N = int(input())
h = list(map(int, input().split()))

DP = [10**10 for _ in range(N)]
DP[0] = 0
DP[1] = abs(h[1]-h[0])

for i in range(2, N):
    DP[i] = min(DP[i-1]+abs(h[i-1]-h[i]), DP[i-2]+abs(h[i-2]-h[i]))
#print(DP)
print(DP[N-1])