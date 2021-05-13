def main():
    numbers = list(map(int, input().split()))
    answer = 0
    if numbers[0] == numbers[1]:
        answer = numbers[2]
    elif numbers[1] == numbers[2]:
        answer = numbers[0]
    else:
        answer = numbers[1]
    print(answer)


if __name__ == '__main__':
    main()

