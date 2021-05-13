# -*- coding: utf-8 -*-

def main():

    S = input()

    listS = list(S)
    listS.sort()

    ans = 'No'
    
    if listS[0] == listS[1] and listS[2] == listS [3] and listS[1] != listS[2]:
        ans = 'Yes'

    print(ans)


if __name__ == "__main__":
    main()