def main():
    x = list(map(int, input().split()))
    counter = 0

    while x[0] % 2 == 0 and x[1] % 2 == 0 and x[2] % 2 == 0:
        if x[0] == x[1] and x[1] == x[2] and x[2] == x[0]:
            counter = -1
            break
        share_0 = x[0] / 2
        share_1 = x[1] / 2
        share_2 = x[2] / 2
        x[0] = share_1 + share_2
        x[1] = share_0 + share_2
        x[2] = share_0 + share_1
        counter += 1

    print(counter)


if __name__ == "__main__":
    main()