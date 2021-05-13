# -*- coding: utf-8 -*-

def main():

    K = int(input())
    A, B = map(int, input().split())

    numA = (A - 1) // K
    numB = B // K

    if numB - numA > 0:
        ans = 'OK'

    else:
        ans = 'NG'

    print(ans)


if __name__ == "__main__":
    main()