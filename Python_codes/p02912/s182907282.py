import heapq
from fractions import Fraction

n, m = list(map(int, input().split()))

a = list(map(lambda x: Fraction(1, int(x)), input().split()))

heapq.heapify(a)

for i in range(m):
    x = heapq.heappop(a)
    y = Fraction(x.numerator * 2, x.denominator)
    if y.numerator < y.denominator:
        heapq.heappush(a, y)
    elif len(a) == 0:
        break

s = 0


for j in range(len(a)):
    s += int(Fraction(a[j].denominator, a[j].numerator))

print(s)
