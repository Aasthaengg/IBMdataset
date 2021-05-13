A = list(map(int, input().split()))
A.sort()
ans = A[2] - A[0]
print(ans)