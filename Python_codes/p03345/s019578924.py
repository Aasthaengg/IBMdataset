def main():
    a, b, c, operation = map(int, input().split())
    answer = a - b
    if abs(answer) > 10 ** 18:
        print("Unfair")
    else:
        if operation % 2:
            print(answer * -1)
        else:
            print(answer)


if __name__ == '__main__':
    main()


