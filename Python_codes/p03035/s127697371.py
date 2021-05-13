inputted = list(map(int, input().split()))
A = int(inputted[0])
B = int(inputted[1])

age = A
full_price = B

is_full_price = age >= 13
is_half_price = 6 <= age <= 12

price = 0
if is_full_price:
    price = full_price
elif is_half_price:
    price = int(full_price / 2)

print(price)
