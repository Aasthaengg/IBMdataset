#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    a = int(input())
    b = int(input())

    if a > b :
        print("GREATER")
    elif a  < b :
        print("LESS")
    elif a  == b :
        print("EQUAL")

if __name__=="__main__":
    main()