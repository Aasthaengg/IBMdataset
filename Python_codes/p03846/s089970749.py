def main():
    people_num = int(input())
    information = sorted(list(map(int, input().split())))
    unique = len(set(information))
    answer = 0
    if unique * 2 == people_num + people_num % 2:
        if people_num > 1 and information[1] > 0:
            answer = 2 ** (unique - people_num % 2)
        elif people_num == 1 and information[0] == 0:
            answer = 1
    print(answer % (10 ** 9 + 7))


if __name__ == '__main__':
    main()

