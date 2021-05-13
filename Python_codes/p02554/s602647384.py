n = int(input())
import math
ans = 0
if n == 1:
    ans =0
if n == 2:
    ans = 2
if n >= 3:
    ans = (10**n%(10**9+7)-9**n%(10**9+7)-9**n%(10**9+7)+8**n%(10**9+7))%(10**9+7)
print(ans)