def main():
    s = input()
    acgt_flag = [0 for i in range(len(s))]

    for i in range(len(s)):
        if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
            acgt_flag[i] = 1

    counter = 0
    counter_max = 0
    for i in range(len(acgt_flag)):
        if acgt_flag[i] == 1:
            counter += 1
            if counter_max < counter:
                counter_max = counter
        else:
            counter = 0

    print(counter_max)


if __name__ == '__main__':
    main()
