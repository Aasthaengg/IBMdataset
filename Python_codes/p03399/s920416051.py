def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())

    train = [A, B]
    train.sort()
    bus = [C, D]
    bus.sort()
    print(train[0] + bus[0])
main()