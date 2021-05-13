n, m = map(int, input().split())
import math
def divisor(n):
    a = set()
    for i in range(1, math.ceil(n**0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return a
d = list(divisor(m))
d.sort(reverse=True)
for di in d:
    if di * n <= m:
        print(di)
        exit()
print(1)