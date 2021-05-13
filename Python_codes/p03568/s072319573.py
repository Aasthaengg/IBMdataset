n = int(input())
A = tuple(map(int, input().split()))
ans = 0
from itertools import product
for P in product([-1, 0, 1], repeat=n):
    B = 1
    for a, p in zip(A, P):
        B *= (a+p)
        if B%2 == 0:
            ans += 1
            break
print(ans)
