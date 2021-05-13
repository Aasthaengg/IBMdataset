import sys
input = sys.stdin.readline
x,a,b = [int(i) for i in input().split()]
da = abs(x-a)
db = abs(x-b)
if da > db :
    print('B')
else :
    print('A')