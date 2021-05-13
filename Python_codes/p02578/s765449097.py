# C - Step

N = int(input())
A = list(int(a) for a in input().split())

ans = 0
if N == 1:
    ans = 0
else:
    for i in range(1, N):
        d = A[i-1] - A[i]
        if d > 0:
            ans += d
            A[i] += d

print(ans)