# -*- coding: utf-8 -*-

def main():

    X, Y = map(int, input().split())

    if Y % 2 == 0 and X * 2 <= Y and Y <= X * 4:
        ans = 'Yes'

    else:
        ans = 'No'

    print(ans)


if __name__ == "__main__":
    main()