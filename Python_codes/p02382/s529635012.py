# -*-coding:utf-8

import math

def main():

    inputNum = int(input())

    x = list(map(float, input().split()))
    y = list(map(float, input().split()))

    absVec = []
    absVec2 = []
    absVec3 = []
    for i, j in zip(x, y):
        absVec.append(abs(i-j))
        absVec2.append(pow(abs(i-j),2))
        absVec3.append(pow(abs(i-j),3))

    print(sum(absVec))
    print(pow(sum(absVec2),1/2))
    print(pow(sum(absVec3),1/3))
    print(max(absVec))

if __name__ == '__main__':
    main()