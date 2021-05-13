import math
def ip():return int(input())
def inp():return map(int,input().split())
def linp():return list(map(int,input().split()))

n=int(input())
g=n%10
s=n//10%10
b=n//100%10
q=n//1000%10
if g==s or s==b or b==q:print("Bad")
else:print("Good")
