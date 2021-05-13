#!/usr/bin/env python3
# -*- coding: utf-8 -*-

OPERATORS = ["+", "-", "*"]


def calc(symbols):
    stack = []
    for s in symbols:
        if s in OPERATORS:
            a = stack.pop()
            b = stack.pop()
            if s == "+":
                stack.append(b + a)
            elif s == "-":
                stack.append(b - a)
            elif s == "*":
                stack.append(b * a)
        else:
            stack.append(int(s))
    return stack[-1]


def main():
    print(calc(input().split()))


if __name__ == "__main__":
    main()