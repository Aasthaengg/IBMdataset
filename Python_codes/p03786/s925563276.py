N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 1
mass = A[0]
for i in range(1, N):
    if A[i] <= 2 * mass:
        ans += 1
    else:
        ans = 1
    mass += A[i]

print(ans)