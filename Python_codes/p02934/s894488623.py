import decimal

N = int(input())
A = list(map(int, input().split()))

rev = [decimal.Decimal(float(1/i)) for i in A]
print(decimal.Decimal(1/sum(rev)))