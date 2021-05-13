# bitが干渉しない範囲
# LごとにRを求める

N = int(input())
A = [int(x) for x in input().split()]

R = -1
S = 0

answer = 0
for L in range(N):
  if R < L:
    R += 1
    S ^= A[L]
  while R<N-1 and not(S & A[R+1]):
    S ^= A[R+1]
    R += 1
  answer += R-L+1
  S ^= A[L]
  
print(answer)