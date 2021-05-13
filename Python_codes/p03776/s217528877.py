from collections import Counter
from math import factorial
n, a, b = map(int, input().split())
v = sorted(list(map(int, input().split())), reverse = True)
max_value = sum(v[:a])/a
cnt1 = Counter(v)[v[a-1]]
cnt2 = Counter(v[:a])[v[a-1]]
comb = factorial(cnt1)//factorial(cnt2)//factorial(cnt1-cnt2)
if v[a-1]==v[0]:
    comb=0
    for i in range(a, min(cnt1, b)+1):
        comb += factorial(cnt1)//factorial(i)//factorial(cnt1-i)
print(max_value)
print(comb)