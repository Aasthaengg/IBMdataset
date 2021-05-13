def main():
    n, c, k = map(int, input().split())
    customers = [int(input()) for i in range(n)]
    
    customers.sort()
    bus_count = 0
    in_bus = []

    for i in range(n):
        if len(in_bus) == 0:
            in_bus.append(customers[i])
        elif len(in_bus) < c and customers[i] <= in_bus[0] + k:
            in_bus.append(customers[i])
        else:
            bus_count += 1
            in_bus = []
            in_bus.append(customers[i])
    
    print(bus_count+1)

if __name__ == '__main__':
    main()