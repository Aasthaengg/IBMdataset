import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n, p = map(int, input().split())
A = list(map(lambda x: int(x) % 2, input().split()))
x = A.count(0)
y = n - x
if p == 1:
    cnt = 0
    for i in range(y + 1):
        if i % 2 == 1:
            cnt += combinations_count(y, i)
    print(2 ** x * cnt)
else:
    cnt = 0
    for i in range(y + 1):
        if i % 2 == 0:
            cnt += combinations_count(y, i)
    print(2 ** x * cnt)