import sys
input = sys.stdin.readline
ma = lambda : map(int,input().split())
ni = lambda : int(input())
a,b,x = ma()

if a<=x and a+b>=x:print("YES")
else:print("NO")
