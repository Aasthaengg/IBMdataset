import sys,math,collections,itertools
input = sys.stdin.readline

X,Y =list(map(int,input().split()))

count = 1
while X<=Y:
    count +=1
    X*=2
print(count-1)
