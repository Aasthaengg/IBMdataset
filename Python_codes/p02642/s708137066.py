N = int(input())
A = list(map(int, input().split()))
A.sort()
MA = max(A)
dp = [True for _ in range(MA+1)]
flag = [False for _ in range(MA+1)]

for i in range(N):
    a = A[i]
    if not flag[a]:
        flag[a] = True
        t = a*2
        while t <= MA:
            dp[t] = False
            t += a
    elif flag[a] == 1:
        dp[a] = False
res = 0
for a in A:
    if dp[a]:
        res += 1
print(res)
