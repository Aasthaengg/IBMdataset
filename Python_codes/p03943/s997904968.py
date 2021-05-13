# -*- coding: utf-8 -*-

def main():

    lists = list(map(int, input().split()))

    lists.sort()

    if lists[2] == lists[1] + lists[0]:
        print('Yes')

    else:
        print('No')


if __name__ == "__main__":
    main()