N, M = map(int, input().split())

ans = 0
if N == 1 and M == 1:
    ans = 1
elif N == 1 and M > 1:
    ans = M-2
elif N > 1 and M == 1:
    ans = N-2
else:
    ans = (N-2)*(M-2)

print(ans)