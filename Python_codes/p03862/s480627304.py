N, x = map(int,input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(0, N-1):
    if A[i] + A[i+1] > x:
        t = A[i+1] + A[i] - x

        if A[i+1] < t:
            A[i+1] = 0
        else:
            A[i+1] -= t
        ans += t

print(ans)