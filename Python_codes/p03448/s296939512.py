def main():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())
    x2 = x // 50
    count = 0
    # 10a + 2b + c = x2

    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if 10 * i + 2 * j + k == x2:
                    count += 1

    print(count)


if __name__ == "__main__":
    main()
