N = int(input())
S = set()
for _ in range(N):
  t = input()
  if t in S:
    S.discard(t)
  else:
    S.add(t)
print(len(S))