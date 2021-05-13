N, K = map(int, input().split())

def solve(N,K):
    ans = (N//K)**3
    if K%2==0:
        ans += (N//(K//2)-N//K)**3
    return ans

print(solve(N,K))