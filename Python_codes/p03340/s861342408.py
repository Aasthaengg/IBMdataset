N = int(input())
A = list(map(int, input().split()))

L, R = 0, 0
S = A[0]
T = A[0]

answer = 0
while L < N and R < N:
  
  if S == T:
    answer += R - L + 1
    R += 1
    if R > N - 1:
      break
    S += A[R]
    T ^= A[R]
  else:
    S -= A[L]
    T ^= A[L]
    L += 1
  #print(L, R, answer)
print(answer)