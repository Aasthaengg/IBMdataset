import re


def main():
    s = input().replace('BC', 'X')
    S = re.split('[BC]', s)
    answer = 0

    for i in S:
        tmp = 0
        for j in i:
            if j == 'A':
                tmp += 1
            else:
                answer += tmp

    print(answer)


if __name__ == '__main__':
    main()