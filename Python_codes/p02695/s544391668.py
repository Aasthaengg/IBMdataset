import itertools
N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for i in range(Q)]
total = []
for A in itertools.combinations_with_replacement(range(1, M+1), N):
  score = 0
  for a,b,c,d in abcd:
    if A[b-1]-A[a-1] == c:
      score += d
    total.append(score)
print(max(total))
