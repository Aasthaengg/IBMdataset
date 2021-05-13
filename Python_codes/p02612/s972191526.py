import math

beer_price = int(input())
bill = math.ceil(beer_price / 1000) * 1000
change = bill - beer_price
print(change)