N = int(input())
A = sorted(int(a) - i for i, a in enumerate(input().split(), 1))
median = A[N // 2]
print(sum(abs(a - median) for a in A))
