n = int(input())
A = list(map(int, input().split()))
A.sort()
A_max = A[-1]
dp = [1] * (A_max + 1)
ans = 0

for i in range(len(A)-1):
    p = A[i]
    if dp[A[i]] == 1:
        for j in range(A_max // p + 1):
            dp[j*p] = 0
        if A[i] != A[i+1]:
            ans += 1
            
if dp[A_max] == 1:
    ans += 1

print(ans)