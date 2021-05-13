import math
def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
a,b = iim()

if 8-min(a,b) < abs(a-b):
    print(':(')
else:
    print('Yay!')