import sys
sys.setrecursionlimit(10**6)

a,b,c=map(int,input().split())

if c<=a+b:
    print("Yes")
else:
    print("No")