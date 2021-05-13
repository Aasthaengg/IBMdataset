def main():
    x = int(input())

    ele = x // 11
    answer = 2 * ele

    if x % 11 != 0:
        x -= 11 * ele
        answer = 2 * ele

        if x <= 6:
            answer += 1
        else:
            answer += 2

    print(answer)


if __name__ == '__main__':
    main()