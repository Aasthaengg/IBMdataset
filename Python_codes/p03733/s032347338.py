n, t = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

ans = 0
til = 0

for i in range(n):
    if A[i] >= til:
        ans += t
    else:
        ans += A[i] - A[i - 1]
    til = A[i] + t


print(ans)
