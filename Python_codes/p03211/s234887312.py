def diff_number(runrun_num: int, master_num: int = 753) -> int:
    return abs(master_num - runrun_num)


def main():
    s = input()
    min_num = int(s[0:3])
    for i in range(3, len(s) + 1):
        runrun_num = int(s[(i - 3):i])

        if diff_number(runrun_num) < diff_number(min_num):
            min_num = runrun_num
    print(diff_number(min_num))


if __name__ == '__main__':
    main()
