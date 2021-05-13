N = int(input())
A = list(map(lambda a: int(a), input().split(" ")))
A.sort()

S = [0] * N
for i in range(N - 1):
  S[A[i] - 1] += 1

print("\n".join([str(s) for s in S]))