#!/usr/bin/env python3


def main():
    n = int(input())
    k = int(input())
    l = list(map(int,input().split()))

    tmp = 0
    for x in l:
        if x <= (k/2):
            tmp+=(2*x)
        else:
            tmp+=(2*(k-x))
    print(tmp)

if __name__ == '__main__':
    main()