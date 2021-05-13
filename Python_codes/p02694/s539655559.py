def N():
    return int(input())
def L():
    return list(map(int,input().split()))
def NL(n):
    return [list(map(int,input().split())) for i in range(n)]
mod = pow(10,9)+7
#import numpy
y = 100
x = N()
cnt = 0
while(1):
    cnt += 1
    y = (y*101)//100
    #print(y)
    if y >= x:
        print(cnt)
        break

