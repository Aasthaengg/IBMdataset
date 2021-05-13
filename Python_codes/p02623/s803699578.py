N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ab_sum , answer, b_i = sum(B), 0, M
for a_i in range(N+1):
  while b_i>0 and ab_sum >K:
    b_i -= 1
    ab_sum -= B[b_i]
  if ab_sum >K:
    break
  answer = max(answer, a_i+b_i)
  if a_i==N:
    break
  ab_sum += A[a_i]

print(answer)
