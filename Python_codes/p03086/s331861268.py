def main():
    s = str(input())
    count = 0
    count_lst = [0]
    flag = False

    for i in range(len(s)):
        letter = s[i]
        string = 'ACGT'

        if letter in string:
            count += 1
            flag = True

        else:
            if flag:
                count_lst.append(count)
            count = 0
            flag = False

    if flag:
        count_lst.append(count)
    longest = max(count_lst)
    print(longest)


if __name__ == '__main__':
    main()