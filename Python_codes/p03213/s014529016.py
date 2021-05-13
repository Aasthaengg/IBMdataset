import math
from collections import Counter

N = int(input())
prime_count = Counter()
def prime(n):
    for i in range(2, math.ceil(math.sqrt(n))+1):
        while n % i == 0:
            n /= i
            prime_count[i] += 1
    if n > 1:
        prime_count[int(n)] += 1   

for i in range(1, N+1):
    prime(i)

ans = 0
# 75, 25, 15, 5, 3, 1
over75, over1 = [], []
for k, v in prime_count.items():
    if v >= 74:
        over75 += [k]
    elif v >= 1:
        over1 += [k]
#ans += len(over75) * len(over1)
#ans += len(over75) * (len(over75)-1)
ans += len(over75)

over25, over3 = [], []
for k, v in prime_count.items():
    if v >= 24:
        over25 += [k]
    elif v >= 2:
        over3 += [k]
ans += len(over25) * len(over3)
ans += len(over25) * (len(over25)-1)

over15, over5 = [], []
for k, v in prime_count.items():
    if v >= 14:
        over15 += [k]
    elif v >= 4:
        over5 += [k]
ans += len(over15) * len(over5)
ans += len(over15) * (len(over15)-1)

over5, over3 = [], []
for k, v in prime_count.items():
    if v >= 4:
        over5 += [k]
    elif v >= 2:
        over3 += [k]
ans += (len(over5) * (len(over5)-1))//2 * len(over3)
ans += len(over5) * ((len(over5)-1) * (len(over5)-2)) // 2
print(ans)