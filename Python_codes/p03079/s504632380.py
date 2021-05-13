# -*- coding: utf-8 -*-

from sys import stdin

def load():
    n = stdin.readline()
    return n

def calc(n):
    return n.count("2")

n = load()
a,b,c = [ int(x) for x in n.split(' ')]

if (a==b and b==c):
    print('Yes')
else:
    print('No')