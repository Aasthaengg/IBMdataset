import math
def ip():return int(input())
def inp():return map(int,input().split())
def inpstr():return map(str,input().split())
def linp():return list(map(int,input().split()))
def linpstr():return list(map(str,input().split()))

s=input()
k=s.find('/')
y=int(s[:k])
s=s[k+1:]
k=s.find('/')
m=int(s[:k])
d=int(s[k+1:])

if y<=2019 and m<=4 and d<=30:
    print("Heisei")
else:print("TBD")
