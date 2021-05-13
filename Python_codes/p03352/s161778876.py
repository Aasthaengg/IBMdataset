def main():
    x = int(input())
    expo_list = []

    for i in range(1, 1000):
        for j in range(2, 10):
            expo_list.append(i ** j)

    expo_list.sort(reverse=True)

    for expo in expo_list:
        if expo <= x:
            print(expo)
            break


if __name__ == "__main__":
    main()
