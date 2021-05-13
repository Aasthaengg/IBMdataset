import math


def main():
    h = int(input())

    counter = 0
    multiple = 1

    while True:
        if h == 1:
            counter += multiple
            break
        else:
            h = math.floor(h/2)
            counter += multiple
            multiple *= 2

    print(counter)


if __name__ == "__main__":
    main()
