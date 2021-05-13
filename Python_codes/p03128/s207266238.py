import sys
input = sys.stdin.readline

#import fractions #fractions.gcd() python~3.4
sys.setrecursionlimit(1000000)

N, M = map(int,input().split())
A = list(map(int, input().split()))
INF = 1e+10
def f(x):
    if x == 1:
        return 2
    if x == 2:
        return 5
    if x == 3:
        return 5
    if x == 4:
        return 4
    if x == 5:
        return 5
    if x == 6:
        return 6
    if x == 7:
        return 3
    if x == 8:
        return 7 
    if x == 9:
        return 6

A.sort(reverse=True)

dp=[-INF]*(N+1)
dp[0] = 0
for i in range(1,N+1):
    for j in range(M):
        if i-f(A[j]) >= 0:
            dp[i] = max(dp[i],dp[i-f(A[j])]+1)
 
ans = ""
remain = dp[N]
match = N

while match > 0:
    for i in range(M):
        if match - f(A[i]) >=0 and dp[match - f(A[i])] == remain - 1:
            ans += str(A[i])
            match -= f(A[i])
            remain -= 1
            
            break
            
print(ans)

