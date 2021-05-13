def main():
    n = int(input())
    has_answered = False
    for x in range(1, 3501):
        if has_answered:
            break
        for y in range(x, 3501):
            if 4 * x * y - n * y - n * x > 0 and (n * x * y) % (4 * x * y - n * y - n * x) == 0:
                print(x, y, (n * x * y) // (4 * x * y - n * y - n * x))
                has_answered = True
                break


if __name__ == '__main__':
    main()

