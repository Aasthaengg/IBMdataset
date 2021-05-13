x = int(input())
a = int(input())
b = int(input())

count_b = (x - a)//b
cash_out = a + b * count_b
cash_rest = x - cash_out

print(cash_rest)