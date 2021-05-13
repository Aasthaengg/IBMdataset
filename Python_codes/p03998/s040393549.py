#!/usr/bin/env python3
a, b, c = open(0).read().split()
n = "a"
while True:
    if eval("len({}) < 1".format(n)):
        print(n.upper())
        break
    exec("n, {0} = {0}[0], {0}[1:]".format(n))
