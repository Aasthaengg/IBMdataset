N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
ans = 0
for i in range(N):
    b = min(A[i], B[i])
    ans += b
    A[i] -= b
    B[i] -= b
    a = min(A[i+1], B[i])
    ans += a
    A[i+1] -= a
    B[i] -= a
print(ans)