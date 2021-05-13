ramen = 700
toppings = list(input())
count = 0

for topping in toppings:
    if topping == "o":
        count += 1

print(700+count*100)