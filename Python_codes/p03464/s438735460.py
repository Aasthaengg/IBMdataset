# coding: utf-8
# Your code here!
import sys

k = int(input())
a = list(map(int,input().split()))[::-1] 
x=2
y=2
if a[0]!=2:
    print(-1)
    sys.exit(0)

for t in a:
    x=((x-1)//t+1)*t
    y=y//t*t+t-1
    #print(x,y) 

if x > y:
    print(-1)
    sys.exit(0)
print(str(x)+" " + str(y)) 