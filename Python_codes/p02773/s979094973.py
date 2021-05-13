N = int(input())
S = {}
for i in range(N):
  tmp = input()
  if tmp in S:
    S[tmp] += 1
  else:
    S[tmp] = 0

l = list(S.items())
l.sort(key=lambda s: (-s[1], s[0]))
M = l[0][1]
print("\n".join([a[0] for a in list(filter(lambda b: b[1] == M, l))]))