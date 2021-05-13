N = int(input())
A = list(map(int, input().split()))

A = sorted([A[i] - i - 1 for i in range(N)])
ans = sum(abs(A[i] - A[N // 2]) for i in range(N))

print(ans)