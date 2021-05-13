N, M = map(int, input().split())
digits = [-1 for _ in range(N+1)]
for __ in range(M):
  digit, num = map(int, input().split())
  if digit == 1 and num == 0 and N != 1:
    print(-1)
    exit()
  elif digits[digit] != -1 and num != digits[digit]:
    print(-1)
    exit()
  else:
    digits[digit] = num
answer = 0
for i in range(1, N+1):
  if digits[i] == -1:
    if i == 1 and N != 1:
      answer += 1*10**(N-i)
  else:
    answer += digits[i]*10**(N-i)
print(answer)
