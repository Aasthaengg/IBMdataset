from math import factorial
from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
b = c.values()
ans = sum([factorial(i)//(factorial(i-2)*2) for i in b if i >= 2])
for i in range(n):
    print(ans-c[a[i]]+1)