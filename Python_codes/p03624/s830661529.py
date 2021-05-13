#!/usr/bin/env python3


def main():
    a = set("abcdefghijklmnopqrstuvwxyz") - set(input())
    if a == set():
        print("None")
        exit(0)
    print(sorted(list(a))[0])


main()
