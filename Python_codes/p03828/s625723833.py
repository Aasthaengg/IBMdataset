from math import factorial
from collections import defaultdict

n = int(input())
cnt = defaultdict(int)
n = factorial(n)
i = 2
while n >= i:
    if n % i == 0:
        n //= i
        cnt[i] += 1
    else:
        i += 1    
ans = 1
#print(cnt)
for k, v in cnt.items():
    ans *= v + 1

print(ans % (10 ** 9 + 7))