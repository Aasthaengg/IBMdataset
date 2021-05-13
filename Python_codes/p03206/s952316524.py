import math
import collections
import sys

#input = sys.stdin.readline
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]

d=I()
print("Christmas" ,end=" ")
for i in range(25-d):
    print("Eve",end=" ")