trains = [int(input()) for i in range(2)]
buses = [int(input()) for i in range(2)]

print(min(trains[0], trains[1]) + min(buses[0], buses[1]))