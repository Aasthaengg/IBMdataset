import math
import itertools
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
p = list(itertools.permutations([A, B, C, D, E], 5))
# print(p)
ans = 10**9
for pi in p:
    order1 = 0
    order2 = math.ceil(pi[0] / 10) * 10
    order3 = math.ceil((order2 + pi[1]) / 10) * 10
    order4 = math.ceil((order3 + pi[2]) / 10) * 10
    order5 = math.ceil((order4 + pi[3]) / 10) * 10
    total = order5 + pi[4]
    ans = min(ans, total)
print(ans)
