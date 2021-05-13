import sys
readline = sys.stdin.readline

A = readline().rstrip()

def nC2(x):
  return (x * (x - 1)) // 2

from collections import defaultdict
dic = defaultdict(int)

for a in A:
  dic[a] += 1
  
ans = nC2(len(A))
for v in dic.values():
  ans -= nC2(v)

print(ans + 1)