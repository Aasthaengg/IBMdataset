from collections import Counter
from math import factorial
n = int(input())
s = [''.join(sorted(list(input()))) for _ in range(n)]

cnt = Counter(s)
ans = 0
for i in cnt.values():
    ans += i*(i-1)//2
print(ans)