def main():
    word = input().replace("BC", "X") + " "
    answer = 0
    count_a = 0
    for i in range(len(word)):
        if word[i] == "A":
            count_a += 1
        elif word[i] == "X":
            answer += count_a
        else:
            count_a = 0
    print(answer)


if __name__ == '__main__':
    main()

