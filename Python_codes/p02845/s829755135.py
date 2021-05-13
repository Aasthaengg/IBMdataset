import sys,math,collections,itertools
input = sys.stdin.readline
 
N=int(input())
A=list(map(int,input().split()))
color1 = -1
color2 = -1
color3 = -1
 
m = 10**9+7
patern = 1
 
for a in A:
    if color1 == a-1 and color2 == a-1 and color3 == a-1:
        patern = (patern * 3)%m
        color1 = a
 
    elif (color1 != a-1 and color2 == a-1 and color3 == a-1):
        patern = (patern * 2)%m
        color2 = a
 
    elif (color1 == a-1 and color2 == a-1 and color3 != a-1):
        patern = (patern * 2)%m
        color1 = a
    elif (color1 == a-1 and color2 != a-1 and color3 != a-1):
        color1 = a
 
    elif (color1 != a-1 and color2 == a-1 and color3 != a-1):
        color2 = a
 
    elif (color1 != a-1 and color2 != a-1 and color3 == a-1):
        color3 = a
 
    elif (color1 != a-1 and color2 != a-1 and color3 != a-1):
        patern = 0
        break
print(patern)
