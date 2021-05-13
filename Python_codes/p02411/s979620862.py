# -*-coding:utf-8

import fileinput
import math

def main():

    while True:
        m, f, r = map(int, input().split())
        if ((m == -1) and (f == -1) and (r == -1)):
            break

        score = m + f
        if ((m == -1) or (f == -1)):
            print('F')
        elif (score >= 80):
            print('A')
        elif (score >= 65):
            print('B')
        elif (score >= 50):
            print('C')
        elif (score >= 30):
            if (r >= 50):
                print('C')
            else:
                print('D')
        else:
            print('F')

if __name__ == '__main__':
    main()