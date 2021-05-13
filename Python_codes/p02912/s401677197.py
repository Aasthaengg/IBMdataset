from fractions import Fraction
from math import log, ceil
import heapq

(n, m), aa = [list(map(int, s.split())) for s in open(0)]
aa = [-Fraction(a) for a in aa]

heapq.heapify(aa)

while m:
    m1 = heapq.heappop(aa)
#     print(f'{m=},{m1=}')
    if len(aa):
        m2 = aa[0]
        use = min(max(ceil(log(m1/m2)/log(2)), 1), m)
#         print(f'{m2=},{use=}')
    else:
        use = min(max(ceil(log(-m1)/log(2)), 1), m)
#         print(f'else, {use=}')
#         print(f'{ceil(log(-m1)/log(2))=}')
#     print(f'{m1/Fraction(2**use)}')
    heapq.heappush(aa, m1 / Fraction(2**use))
    m -= use
    if -(aa[0]) < 1:
        break

aa = [int(-a) for a in aa]

print(sum(aa))