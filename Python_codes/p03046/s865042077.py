M, K =map(int, input().split())
if K >= 2**M:
    ans = [-1]
elif M == 0:
    ans = [0, 0]
elif M == 1:
    if K == 1:
        ans = [-1]
    else:
        ans = [0, 0, 1, 1]
else:
    ans = list(range(K)) + list(range(K+1, 2**M)) +[K] + list(range(2**M-1, K, -1))+list(range(K-1, -1, -1)) +[K]
print(*ans)