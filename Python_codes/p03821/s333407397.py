N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
ans = 0
for i in range(N-1, -1, -1):
    A[i] += ans
    ans += B[i] - (A[i] % B[i]) if A[i] % B[i] != 0 else 0
# print(A)
print(ans)
