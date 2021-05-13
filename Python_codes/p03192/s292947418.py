# -*- coding: utf-8 -*-

from sys import stdin

def load():
    n = stdin.readline()
    return n

def calc(n):
    return n.count("2")

n = load()
print(calc(n))