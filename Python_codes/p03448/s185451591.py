A = int(input())
B = int(input())
C = int(input())
X = int(input())

import itertools as it
ans = 0
for a,b,c in it.product(range(A+1), range(B+1), range(C+1)):
    if 500*a + 100*b + 50*c == X:
        ans += 1
print(ans)