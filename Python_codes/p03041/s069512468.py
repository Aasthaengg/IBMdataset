import math
def ip():return int(input())
def inp():return map(int,input().split())
def linp():return list(map(int,input().split()))

n,k=inp()
s=[x for x in input()]
s[k-1]=chr(ord(s[k-1])+32)
for x in s:print(x,end="")
