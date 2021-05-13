N = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = tuple(map(int, input().split()))
assert len(A) == N
assert len(B) == N
assert len(C) == N - 1

score = sum([B[a-1] for a in A])
for A1,A2 in zip(A, A[1:]):
  if A2 == A1 + 1:
    score += C[A1-1]
print(score)