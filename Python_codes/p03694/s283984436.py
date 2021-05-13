N = int(input())
A = list(map(int, input().split()))

A = sorted(A)
ans = A[-1] - A[0]

print(ans)



