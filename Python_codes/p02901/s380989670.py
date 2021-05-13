n, m = map(int, input().split())
A = [0]*m
C = [0]*m
for i in range(m):
    a, b = map(int, input().split())
    A[i] = a
    c = list(map(int, input().split()))
    c = [x-1 for x in c]
    C[i] = c


dp = [10**18]*(2**n)
dp[0] = 0
C_bit = [0]*m
for i in range(m):
    C_bit[i] = 0
    for j in C[i]:
        C_bit[i] += 2**j

for i in range(2**n):
    for j in range(m):
        ni = i | C_bit[j]
        dp[ni] = min(dp[ni], dp[i]+A[j])

if dp[-1] == 10**18:
    print(-1)
else:
    print(dp[-1])