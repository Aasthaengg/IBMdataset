import sys,math
input = sys.stdin.readline

a,b = list(map(int,input().split()))
print(math.ceil((a+b)/2))
