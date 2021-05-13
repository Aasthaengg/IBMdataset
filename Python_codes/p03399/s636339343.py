original_train_fee = int(input())
fixed_train_fee = int(input())
original_bus_fee = int(input())
fixed_bus_fee = int(input())

total_price = min(original_train_fee, fixed_train_fee) + min(original_bus_fee, fixed_bus_fee)
print(total_price)