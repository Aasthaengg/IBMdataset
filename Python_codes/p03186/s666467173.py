import sys
input=sys.stdin.readline

a,b,c = map(int, input().split())

if a >= c-1 or b >= c-1 or a+b >= c-1:
    print(b+c)
else:
    print(b+(a+b)+1)
