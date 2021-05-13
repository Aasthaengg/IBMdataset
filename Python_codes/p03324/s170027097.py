import sys

input = sys.stdin.readline

d, n= map(int, input().split())
if n == 100:
    print(101*100**d)
    exit(0)
print(100**d*n)
