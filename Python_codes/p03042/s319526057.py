# -*- coding: utf-8 -*-

def main():

    S = input()

    listS = [int(S[:2]), int(S[2:])]

    if 1 <= listS[0] <= 12 and 1 <= listS[1] <= 12:
        ans = 'AMBIGUOUS'

    elif 1 <= listS[0] <= 12:
        ans = 'MMYY'

    elif 1 <= listS[1] <= 12:
        ans = 'YYMM'

    else:
        ans = 'NA'

    print(ans)


if __name__ == "__main__":
    main()