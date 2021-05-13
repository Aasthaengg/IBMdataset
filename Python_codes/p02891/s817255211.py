def main():
    word = input()
    repeat = int(input())
    count_succession = 1
    before = word[0]
    base = 0
    for w in word[1:] + " ":
        if before == w:
            count_succession += 1
        else:
            before = w
            base += count_succession // 2
            count_succession = 1
    answer = repeat * base
    if len(set(list(word))) == 1:
        answer = repeat * len(word) // 2
    elif word[-1] == word[0]:
        succession_begin = 0
        succession_end = 0
        for i in range(1, len(word)):
            if word[i] != word[0]:
                succession_begin = i
                break
        for i in range(-2, -len(word) - 1, -1):
            if word[i] != word[-1]:
                succession_end = -i - 1
                break
        answer -= (succession_begin // 2 + succession_end // 2 - (succession_begin + succession_end) // 2) * (repeat - 1)
    print(answer)


if __name__ == '__main__':
    main()

