import sys

a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())

d1 = (v - w)*t
d2 = abs(a-b) 
if v < w:
    print("NO")
elif d1 >= d2 :
    print("YES")
else:
    print('NO')