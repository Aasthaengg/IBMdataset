#!/usr/bin/env python3
def main():
    H, _ = map(int, input().split())
    offence = sum([int(x) for x in input().split()])
    print('Yes' if H <= offence else 'No')


if __name__ == '__main__':
    main()
