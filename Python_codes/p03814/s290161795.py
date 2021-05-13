#!/usr/bin/env python3


def main():
    s = input()
    print(s.rindex("Z") - s.index("A") + 1)


main()
