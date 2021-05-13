# coding: utf-8
# Your code here!

import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

d = I()
contest = LI()
mylist = [LI() for i in range(d)]
day = [0] * 26
result = 0

for i in range(d):
    temp = I()
    result += mylist[i][temp-1]
    day = [j+1 for j in day]
    day[temp-1] = 0
    for k in range(26):
        result -= day[k] * contest[k]
    print(result)