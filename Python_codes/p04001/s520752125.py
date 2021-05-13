# ARC061A

import itertools

s = list(input())
n = len(s)
bin = list(itertools.product(['', '+'''], repeat=n - 1))
count = 0
for i in bin:
    t = []
    for j in range(n-1):
        t.append(s[j])
        t.append(i[j])
    t.append(s[-1])
    formula = ''.join(t)
    # print(t)
    count += eval(formula)
print(count)
