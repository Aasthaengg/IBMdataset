#import math

a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())

ans=a+t*v>=b+t*w and a-t*v<=b-t*w
print('YES' if ans else 'NO')
