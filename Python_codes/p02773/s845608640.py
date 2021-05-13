from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

S = Counter(S).most_common()
l = []
for i in S:
  if i[1] == S[0][1]: l.append(i[0])

l = sorted(l)
for i in l:
  print(i)