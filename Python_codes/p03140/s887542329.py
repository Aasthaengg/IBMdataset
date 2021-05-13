def main():
    length = int(input())
    words = [input() for _ in range(3)]
    answer = 0
    for i in range(length):
        l = [words[0][i], words[1][i], words[2][i]]
        answer += len(set(l)) - 1
    print(answer)


if __name__ == '__main__':
    main()

