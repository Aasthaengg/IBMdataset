import sys

input = sys.stdin.readline

n, a, b= map(int, input().split())

if (b-a)%2 ==0:
    print((b-a)//2)

else:
    min_sabun = min(a-1,n-b)
    kyori = (b-a-1)//2
    print(min_sabun+kyori+1)