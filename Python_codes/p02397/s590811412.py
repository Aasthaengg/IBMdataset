data = [int(x) for x in input().split()]
while(not(data[0] == 0 and data[1] == 0)):
    data.sort()
    print(data[0], data[1])
    data = [int(x) for x in input().split()]