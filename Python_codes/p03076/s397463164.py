import math
from itertools import permutations
A = [int(input()) for _ in range(5)]

ans = float("inf")
for a in permutations(A, 5):
    m = 0
    for i in a:
        m = math.ceil(m/10)*10
        m += i
    ans = min(ans, m)
print(ans)
