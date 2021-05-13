import sys
import math


def input():
    return sys.stdin.readline().rstrip()


def main():

    A,B,K =map(int,input().split())

    count = 0
    for i in range(101,0,-1):
        if A%i ==0 and B% i ==0:
            count +=1

        if count ==K:
            print(i)
            exit()



if __name__ == "__main__":
    main()
