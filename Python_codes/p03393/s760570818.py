# https://atcoder.jp/contests/agc022/tasks/agc022_a

import sys
s = input()
A = [chr(ord("a") + i) for i in range(26)]
if len(s) < 26:
  for a in A:
    if a not in s:
      print(s + a)
      sys.exit()
else:
  for p in range(26)[::-1]:
    for a in A[A.index(s[p])+1:]:
      if a not in s[:p]:
        print(s[:p] + a)
        sys.exit()
print(-1)
