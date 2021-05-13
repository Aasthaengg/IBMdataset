#!/usr/bin/env python3


def main():
    a,v = map(int,input().split())
    b,w = map(int,input().split())
    t = int(input())

    if w >= v:
        print("NO")
    elif abs(b-a)/(v-w) <= t:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()