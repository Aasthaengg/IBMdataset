N = int(input())
A = map(int, input().split(' '))

import collections
n_frq_dict = collections.Counter(A)

ans = 0
negative = 0
for n, frq in n_frq_dict.items():
    if frq % 2 == 1:
        ans += 1
    else:
        ans += 1
        negative += 1

print(ans - negative % 2)