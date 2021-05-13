def main():
    x = int(input())
    theta = 360
    k = 0

    while True:
        if theta % x == 0:
            k = theta // x
            break
        theta += 360

    print(k)


if __name__ == "__main__":
    main()
