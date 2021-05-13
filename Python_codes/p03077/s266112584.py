n = int(input())
buses = [int(input())for i in range(5)]
buses.sort()
capa = n//buses[0] if n/buses[0] != n//buses[0] else n//buses[0]-1
print(5+capa)