N = int(input())

answer = 0
for n in range(1, int(N**0.5)+1):
  m = N//n if N%n != 0 else N//n-1
  if m >= n:
    answer += (m-n+1)*2-1
print(answer)