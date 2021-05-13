def main():
    x = int(input())

    answer = 0
    tmp = 0
    for i in range(10 ** 9):
        tmp += i
        if tmp >= x:
            answer = i
            break

    print(answer)


if __name__ == '__main__':
    main()