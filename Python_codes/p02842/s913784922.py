from decimal import Decimal
N = int(input())
a = Decimal('1.08')
for x in range(N+1):
    if int(x*a) == N:
        print(x)
        exit()

print(':(')