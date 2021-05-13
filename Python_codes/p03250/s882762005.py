A = list(map(int, input().split()))
A = sorted(A)
ans = A[0] + A[1] + 10 * A[2]
print(ans)
