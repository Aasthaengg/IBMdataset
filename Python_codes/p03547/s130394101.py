import sys
input = sys.stdin.readline

X,Y=list(input().rstrip().split())
if X>Y:
    print('>')
elif X<Y:
    print('<')
else:
    print('=')
