# -*- coding: utf-8 -*-

def main():

    N = int(input())

    case1 = [2, 4, 5, 7, 9]
    case2 = [0, 1, 6, 8]
    case3 = [3]

    num = N % 10

    if num in case1:
        ans = 'hon'

    elif num in case2:
        ans = 'pon'

    elif num in case3:
        ans = 'bon'

    print(ans)


if __name__ == "__main__":
    main()