# -*- coding: utf-8 -*-

def main():

    A, B = map(int,input().split())

    if A <= 9 and B <= 9:
        ans = A * B

    else:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()