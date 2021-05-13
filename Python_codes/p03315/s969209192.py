#!/usr/bin/env python3
import sys

def main():
    answer = 0
    a = input()
    answer = answer + a.count("+") - a.count("-")
    print(answer)

if __name__ == '__main__':
    main()
