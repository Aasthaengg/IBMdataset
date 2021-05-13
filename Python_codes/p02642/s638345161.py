N = int(input())
A = sorted(list(map(int, input().split(' '))))
# print(A)
a_max = A[-1]
dp = [True]*(a_max+1)
ans = 0
for i in range(N-1):
    p = A[i]
    if dp[p] == True:
        # print(math.sqrt(p))
        for q in range(a_max//p+1):
            # print(p*q)
            dp[p*q] = False
        if A[i] != A[i+1]:
            ans += 1
if dp[A[-1]]:
    ans += 1
print(ans)
