N = int(input())
S = input()
MOD = 10 ** 9 + 7
from collections import defaultdict
dic = defaultdict(int)

for s in S:
  dic[s] += 1
  
ans = 1
for value in dic.values():
  ans *= (value + 1)
  ans %= MOD
  
print((ans - 1) % MOD)