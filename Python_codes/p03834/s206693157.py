#!/usr/bin/env python3
# coding:utf-8

def main():
    stdIn = input()
    stdOut = solve(stdIn)
    print(stdOut)


def solve(stdIn):
    return stdIn.replace(',',' ')

if __name__ == "__main__":
    main()
