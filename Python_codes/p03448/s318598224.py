def main(n500, n100, n50, price):
    count = 0
    for i in range(n500 + 1):
        if i * 500 <= price:
            for j in range(n100 + 1):
                if i * 500 + j * 100 <= price:
                    for k in range(n50 + 1):
                        p = i * 500 + j * 100 + k * 50
                        if p == price:
                            count += 1
    print(count)


if __name__ == "__main__":
    n500 = int(input())
    n100 = int(input())
    n50 = int(input())
    price = int(input())
    main(n500, n100, n50, price)
