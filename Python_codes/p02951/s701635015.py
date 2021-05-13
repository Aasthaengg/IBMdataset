# -*- coding: utf-8 -*-

def main():

    A, B, C = map(int, input().split())

    L = C - (A - B)

    if L <+ 0:
        ans = 0

    else:
        ans = L

    print(ans)


if __name__ == "__main__":
    main()