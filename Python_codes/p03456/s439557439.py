#-*-coding:utf-8-*-
import sys
import math
input=sys.stdin.readline

def main():
    a,b = input().split()
    number=0

    number=int(a+b)
    for i in range(100101):
        if i * i ==number:
            print("Yes")
            exit()
        else:
            continue
    print("No")


if __name__=="__main__":
    main()