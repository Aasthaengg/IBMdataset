import bisect,copy,heapq,itertools,string
from collections import *
from math import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n, a, b, c, d = MAP()
s = 'a' + input()

flag = 0
for i in range(min(a,b)+1,max(c,d)):
        if (a < i < c or b < i < d) and s[i] == s[i-1] == '#':
                print("No")
                exit()       
        elif max(a,b) <= i <= min(c,d) and s[i-1] == s[i] == s[i+1] == '.':
                flag = 1

if c > d and flag == 0:
        print("No")
else:
        print("Yes")