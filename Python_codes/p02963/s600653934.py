import sys
input=sys.stdin.readline

s=int(input())

#0<= x,y <=10**9
#s/2

if s<=10**9:
    print(0,0,1,0,0,s)
    exit()

y=(-1*s//(10**9))*(-1)
x=10**9*y-s

print(0,0,10**9,1,x,y)


