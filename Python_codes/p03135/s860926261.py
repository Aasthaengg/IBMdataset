import decimal

tx = input()
tx = tx.split()
t = int(tx[0])
x = int(tx[1])
result = decimal.Decimal(t/x)
print(result)