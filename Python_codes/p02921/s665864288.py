import sys
input = sys.stdin.readline
import math
import collections
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

s=input()
t=input()
count=0
for i in range(3):
    if s[i:i+1]==t[i:i+1]:
        count+=1
print(count)
