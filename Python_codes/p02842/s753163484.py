#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

import decimal

def main():
    tax = decimal.Decimal('1.08')
    n = int(input())

    for i in range(1,n+1):
        if int(i*tax)==n:
            print(i)
            exit()
        else:
            continue
    print(":(")

if __name__=="__main__":
    main()