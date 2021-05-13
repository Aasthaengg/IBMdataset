#!/usr/bin/env python3
import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    print('Yay!' if all(map(lambda x:True if int(x)<9 else False, input().split())) else ':(')
    


if __name__ == '__main__':
    main()

