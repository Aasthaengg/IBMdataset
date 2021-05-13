## B - Iron Bar Cutting
N = int(input())
A = list(map(int, input().split()))
L = 0
R = sum(A)
ans = sum(A)
for n in range(N):
    L += A[n]
    R -= A[n]
    if ans > abs(L-R):
        ans = abs(L-R)
print(ans)