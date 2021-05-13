# -*- coding: utf-8 -*-

def main():

    A = list(map(int, input().split()))

    sumA = sum(A)

    if sumA >= 22:
        ans = 'bust'

    else:
        ans = 'win'

    print(ans)


if __name__ == "__main__":
    main()