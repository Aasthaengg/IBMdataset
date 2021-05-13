from string import ascii_lowercase


def main():
    word = input()
    if len(word) < 26:
        count = {}
        for a in ascii_lowercase:
            count[a] = 0
        for w in word:
            count[w] += 1
        count_l = list(count.items())
        count_l.sort(key=lambda x: x[0])
        add = ""
        for i in range(26):
            if count_l[i][1] == 0:
                add = count_l[i][0]
                break
        print(word + add)
    elif word == ascii_lowercase[::-1]:
        print(-1)
    else:
        is_printed = False
        while len(word) > 0 and not is_printed:
            for c in ascii_lowercase[ascii_lowercase.index(word[-1]) + 1:]:
                if c not in word[:-1]:
                    print(word[:-1] + c)
                    is_printed = True
                    break
            else:
                word = word[:-1]


if __name__ == '__main__':
    main()

