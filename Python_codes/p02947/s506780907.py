from collections import Counter
from math import factorial
n = int(input())
s = [''.join(sorted(list(input()))) for _ in range(n)]

def combination(i):
    return factorial(i) // (factorial(i-2) * factorial(2))

cnt = Counter(s)
ans = 0
for i in cnt.values():
    if i == 1:
        pass
    else:
        ans += combination(i)
print(ans)