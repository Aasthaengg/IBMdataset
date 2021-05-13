N, x = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

for i in range(1, N):
    s = A[i] + A[i-1]
    if s > x:
        y = s-x
        if A[i] > y:
            A[i] -= y
            A[i-1] -= y
            ans += y
        else:
            z = y - A[i]
            A[i] = 0
            A[i-1] -= A[i]
            A[i-1] -= z
            if i >= 2:
                A[i-2] -= z
            ans += y
print(ans)


