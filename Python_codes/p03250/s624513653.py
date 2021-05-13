def main():
    numbers = list(map(int, input().split()))

    numbers = sorted(numbers)[::-1]

    print(int(str(numbers[0]) + str(numbers[1])) + numbers[2])

if __name__ == '__main__':
    main()