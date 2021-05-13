# -*- coding: utf-8 -*-

def main():

    S = input()
    listS = list(S)

    if listS[2] == listS[3] and listS[4] == listS[5]:
        ans = 'Yes'

    else:
        ans = 'No'

    print(ans)


if __name__ == "__main__":
    main()