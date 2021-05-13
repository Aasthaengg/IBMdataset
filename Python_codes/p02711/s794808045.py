# -*- coding: utf-8 -*-

def main():

    N = int(input())

    listN = list(map(int, str(N)))

    if 7 in listN:
        ans = 'Yes'

    else:
        ans = 'No'

    print(ans)


if __name__ == "__main__":
    main()