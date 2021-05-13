def main():
    num = int(input())
    counter = [0] * (num + 1)
    # func(41, 41, 41) = 10086
    # func(99, 1, 1) = 10002
    for x in range(1, 100):
        for y in range(1, 100):
            for z in range(1, 123 - x - y + 1):
                tmp = (x + y + z) ** 2 - x * y - y * z - z * x
                if tmp > num:
                    break
                counter[tmp] += 1
    for count in counter[1:]:
        print(count)


if __name__ == '__main__':
    main()
