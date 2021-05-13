N = int(input())
P = []
for i in range(N):
  P.append(int(input()))
#print(P)

S = [0 for _ in range(N+1)]
for i in range(N):
  S[P[i]] = S[P[i]-1] + 1
print(N-max(S))
