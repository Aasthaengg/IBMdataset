import sys
from bisect import bisect_left as bl
input = sys.stdin.readline
S = list(input())[: -1]
table = [[] for _ in range(26)]
a = ord("a")
res = 1
for i in range(len(S)):
  table[ord(S[i]) - a].append(i)
for i in range(len(S)):
  x = bl(table[ord(S[i]) - a], i)
  res += len(S) - (len(table[ord(S[i]) - a]) - x) - i
  #print(res, (len(table[ord(S[i]) - a]) - x))
print(res)