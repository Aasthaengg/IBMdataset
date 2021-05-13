S = [(ord("z") + 1 - ord(s)) % 26 for s in input()]
K = int(input())

for i in range(len(S)):
  if S[i] > K: continue
  K -= S[i]
  S[i] = 0

S[-1] = (S[-1] - K) % 26
print(*[chr(ord("z") - (s-1) % 26) for s in S], sep="")