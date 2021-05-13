from itertools import groupby, accumulate, product, permutations, combinations
def solve():
    ans = 0
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = [0]+list(accumulate(A))
    B = [0]+list(accumulate(B))
    b = M
    for a in range(N+1):
        if A[a]>K:
            break
        while A[a]+B[b]>K:
            b -= 1
        ans = max(a+b,ans)
    return ans
print(solve())
