#!/usr/bin/env python3


def main():
    S = input()
    if S[0] == S[1]:
        print('Bad')
    elif S[1] == S[2]:
        print('Bad')
    elif S[2] == S[3]:
        print('Bad')
    else:
        print('Good')


if __name__ == '__main__':
    main()
