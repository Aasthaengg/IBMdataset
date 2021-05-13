n = int(input())
a = list(map(int, input().split()))
N = [0] * (n+1)
for i in range(1, n+1):
    N[i] += N[i-1] + a[i-1]

Max = N[-1]
ans = float("INF")
for i in range(1, n):
    if abs(N[i] - (Max-N[i])) < ans:
        ans =  abs(N[i] - (Max-N[i]))
print(ans)