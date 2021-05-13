MOD = 10 ** 9 + 7

def solve():
    N, K = map(int, input().split())
    A = list((map(int, input().split())))
    
    ans = 0
    for i, ai in enumerate(A):
        left = 0
        right = 0
        for j in range(i):
            if ai > A[j]:
                left += 1
        for j in range(i+1, N):
            if ai > A[j]:
                right += 1
        
        ans += (K*(K+1)*right//2) + (K*(K-1)*left//2)
        
    return ans % MOD
    
print(solve())