from collections import Counter
N = int(input())
A = [int(c) for c in input().split()]
ans = 1
MOD = 10**9+7
Cnt = Counter(A)
if N%2==1:
  for k,v in Cnt.items():
    if (k%2==0 and v==2) or (k==0 and v==1):
      ans *= v
      ans %= MOD
    else:
      print(0)
      break
  else:
    print(ans)
else:
  for k,v in Cnt.items():
    if k%2==1 and v==2:
      ans *= v
      ans %= MOD
    else:
      print(0)
      break
  else:
    print(ans)