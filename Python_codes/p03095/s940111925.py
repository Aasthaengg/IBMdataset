from collections import Counter
MOD = 10**9 + 7
n = int(input())
c = Counter(input())
ans = 1
for k,v in c.items():
  ans = (ans*(v+1)) % MOD
  
print(ans-1)