def main():
    length = int(input())
    stones = list(input())
    white = [0] * length
    if stones[0] == ".":
        white[0] = 1
    for i in range(1, length):
        if stones[i] == ".":
            white[i] = white[i - 1] + 1
        else:
            white[i] = white[i - 1]
    answer = min(white[-1], length - white[-1])
    for i in range(length):
        answer = min(answer, i + 1 + white[-1] - 2 * white[i])
    print(answer)


if __name__ == '__main__':
    main()

