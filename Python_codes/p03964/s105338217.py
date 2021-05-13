import sys
input = sys.stdin.readline
n=int(input())
T=1
A=1

for i in range(n):
    t,a=map(int,input().split())
    x=-(-T//t)
    y=-(-A//a)
    bai=max(x,y)
    T=t*bai
    A=a*bai
print(T+A)
