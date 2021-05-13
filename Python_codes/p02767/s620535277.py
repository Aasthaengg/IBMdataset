from sys import stdin
from decimal import Decimal, ROUND_HALF_UP

n = int(stdin.readline().rstrip())
data = list(map(int, stdin.readline().rstrip().split()))
p = sum(data) / n

#p should be int
p_int = (Decimal(p).quantize(Decimal('1'), ROUND_HALF_UP))

Sum = 0
for i in data:
	Sum  += (i - p_int) ** 2 
print(Sum)