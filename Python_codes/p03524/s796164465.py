import sys
import os

def file_input():
    f = open('CODE_FESTIVAL_2017Final/input.txt', 'r')
    sys.stdin = f

def main():
    #file_input()
    S=input()

    a=b=c=0

    for s in S:
        if s=='a':
            a+=1
        elif s=='b':
            b+=1
        else:
            c+=1

    if max(a,b,c)-min(a,b,c)<=1:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
