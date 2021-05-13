N = int(input())
A = []
B = []

for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

A = sorted(A)
B = sorted(B)

if N % 2:
    ans = B[N//2] - A[N//2] + 1
else:
    l = A[N//2-1] + A[N//2]
    r = B[N//2-1] + B[N//2]
    ans = r-l+1
print(ans)