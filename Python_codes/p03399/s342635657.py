trainA = int(input())
trainB = int(input())
busA = int(input())
busB = int(input())

train_min = min(trainA, trainB)
bus_min = min(busA, busB)

min_price = train_min + bus_min

print(min_price)