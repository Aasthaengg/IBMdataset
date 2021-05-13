import sys
input=sys.stdin.readline

k=int(input())

print(50)
x=k//50
y=k%50

a=49+x
for i in range(50-y):
    print(a-y,end='')
    print(' ',end='')
for i in range(y):
    print(a+51-y,end='')
    print(' ',end='')