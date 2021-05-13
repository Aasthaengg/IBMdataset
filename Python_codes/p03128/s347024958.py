a = [2, 5, 5, 4, 5, 6, 3, 7, 6]
N, M = list(map(int, input().split()))
A = sorted(set(list(map(int, input().split()))), reverse=True)
B = sorted([a[i-1] for i in A])

dp = [-1] * (N+1)
for b in B:
    if b < N+1:
        dp[b] = 1

for i in range(1, N+1):
    for b in B:
        if i < b:
            break
        else:
            dp[i] = max(dp[i], dp[i-b]+1)
digit = dp[-1]

for n in A:
    x = a[n-1]
    if N-x >= 0:
        while dp[N-x] == digit-1:
            print(n, end='')
            N -= x
            digit -= 1
        if N == x:
            print(n, end='')
            N -= x