# -*- coding: utf-8 -*-

def main():

    s = input()
    listS = list(s)
    n = len(listS)

    aIndex = 0
    zIndex = 0

    for i in range(n):
        if listS[i] == 'A':
            aIndex = i
            break

    for i in range(n):
        if listS[-(i + 1)] == 'Z':
            zIndex = n - i
            break

    ans = zIndex - aIndex

    print(ans)


if __name__ == "__main__":
    main()