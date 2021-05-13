N, K = map(int, input().split())
A = list(map(int, input().split()))

def solve(N,K,A):
    ans = -(-(N-1)//(K-1))
    return ans
print(solve(N,K,A))