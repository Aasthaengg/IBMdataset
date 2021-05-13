n, a, b = map(int, input().split())

a_fee = a * n
b_fee = b

if a_fee < b_fee:
    print(a_fee)
else:
    print(b_fee)