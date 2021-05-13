import collections

N, M = map(int, input().split())
A = list(map(int, input().split()))

S = [0]
for i in range(N):
  S.append(S[i] + A[i])
S = S[1::]
#print("S:", S)

S = list(map(lambda x: x % M, S))
S = collections.Counter(S).items()
#print("S:", S)

answer = 0
for k, v in S:
  if k == 0:
    answer += v * (v + 1) //2
  else:
    answer += v * (v - 1) //2
print(answer)