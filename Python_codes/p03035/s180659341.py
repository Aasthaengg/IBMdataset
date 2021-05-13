line = input()
A, B = [int(n) for n in line.split()]
price = B if A >= 13 else int(B/2) if (A >= 6 and A<=12) else 0
print(price)