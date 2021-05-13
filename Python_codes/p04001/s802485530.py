# coding: utf-8
# Your code here!
import sys
input = sys.stdin.readline
import itertools
 
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

s = str(input().rstrip())
s = tuple(int(s[i]) for i in range(len(s)))


mylist = [1, 0]
d = []

for i in itertools.product(mylist, repeat = len(s)-1):
    temp = s[0]
    result = 0
    for j, k in zip(s[1:], i):
        if k != 1:
            temp = temp * 10 + j
        else:
            result += temp
            temp = j
    result += temp
    d.append(result)
    
print(sum(d))