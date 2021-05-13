#!/usr/bin/ python3.8
N=int(input())
d=[int(x) for x in input().split()]
d.sort()
if N%2==1:
    print(0)
    exit(0)
x,y=d[N//2-1:N//2+1]
print(y-x)
