N, M = map(int,input().split())
if N > M:
    N, M = M, N
if N == 1:
    if M == 1:
        ans = 1
    else:
        ans = M - 2
elif N == 2:
    ans = 0
else:
    ans = (N - 2) * (M - 2)
print(ans)