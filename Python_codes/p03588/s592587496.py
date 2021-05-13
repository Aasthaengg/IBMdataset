import sys
input=sys.stdin.readline

n=int(input())
x=0
y=10**10
for _ in range(n):
    a,b=map(int,input().split())
    if x<=a:
        x=a
        y=b
print(x+y)
