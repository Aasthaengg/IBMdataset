# -*- coding: utf-8 -*-

while True:
    line = map(str, raw_input().split())
    x = int(line[0])
    op = line[1]
    y = int(line[2])
    if op == "?":
        break
    elif op == "+":
        print x+y
    elif op == "-":
        print x-y
    elif op == "*":
        print x*y
    elif op == "/":
        print x/y