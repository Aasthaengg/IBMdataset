import math

A, B, C = list(map(int, input().split()))

price = A
possession = B
maximum = C

number_of_purchases = min(math.floor(B / A), maximum)

print(number_of_purchases)
