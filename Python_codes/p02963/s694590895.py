import math
S = int(input())
ss = math.ceil(math.sqrt(S))
print('{} {} {} {} {} {}'.format(ss, ss ** 2 - S, 1, ss, 0, 0))