# -*- coding: utf-8 -*-
from sys import stdin
from operator import itemgetter
import math
# stdin = open("sample.txt")

a = int(stdin.readline().rstrip())
b = int(stdin.readline().rstrip())
h = int(stdin.readline().rstrip())
print((a+b)*h//2)