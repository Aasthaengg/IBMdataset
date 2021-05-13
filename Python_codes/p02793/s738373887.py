n = int(input())

import fractions
import collections
a = collections.deque(list(map(int, input().split())))
 
lcm = a.popleft()
a.append(lcm)
for i in range(1, n):
    tem = a.popleft()
    lcm = lcm * tem // fractions.gcd(lcm, tem)
    a.append(tem)
 
ans = 0
for i in range(n):
    tem = a.popleft()
    ans += lcm // tem
 
print(ans % (10**9+7))