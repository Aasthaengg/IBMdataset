import math
n = int(input())
m = int(math.sqrt(8 * n + 1))

if m * m != 8 * n + 1:
  print("No")
else:
  k = int((m + 1) / 2)
  S = [[] for h in range(k)]
  l = 1
  for i in range(k - 1):
    for j in range(i + 1, k):
      S[i].append(l)
      S[j].append(l)
      l += 1
  print("Yes")
  print(k)
  s = "{} " * k
  t = s.rstrip(" ")
  for p in range(k):
    print(t.format(k - 1, *S[p]))