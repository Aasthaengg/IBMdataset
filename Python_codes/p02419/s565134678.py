# -*-coding:utf-8

import fileinput

def main():

    W = input().lower()

    count = 0
    while True:
        T = input()
        if(T == 'END_OF_TEXT'):
            break
        inputList = T.lower().split()

        for i in inputList:
            if(W == i):
                count += 1

    print(count)

if __name__ == '__main__':
    main()