import itertools
import math
import fractions
import functools
n = input()
ans = []

for i in range(len(n)):
    if n[i] == '1':
        ans.append('9')
    else: ans.append('1')
print(''.join(ans))