import math
def ip():return int(input())
def inp():return map(int,input().split())
def linp():return list(map(int,input().split()))

s=input()
if s[0]==s[1] or s[1]==s[2] or s[2]==s[3]:
    print("Bad")
else:print("Good")