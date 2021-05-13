N, K = map(int, input().split())
answer = 0

for b in range(K+1, N+1):
  # print(b, (b-K)*(N//b)+max(0, N%b-K+1))
  if K == 0:
    answer += N%b
  else:
    answer += max(0, N%b-K+1)
  answer += (b-K)*(N//b)
print(answer)