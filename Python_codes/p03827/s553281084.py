# -*- coding: utf-8 -*-

def main():

    N = int(input())
    S = input()

    listS = list(S)
    x = 0
    listNum = [x]

    for i in listS:
        if i == 'I':
            x += 1
            listNum.append(x)

        elif i == 'D':
            x += -1
            listNum.append(x)

    ans = max(listNum)
    print(ans)


if __name__ == "__main__":
    main()