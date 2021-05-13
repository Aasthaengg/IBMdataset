N, K = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])
ans = float('inf')

for i in range(N+1-K):
    ans = min(ans,abs(arr[i]-arr[i+K-1]))
print(ans)