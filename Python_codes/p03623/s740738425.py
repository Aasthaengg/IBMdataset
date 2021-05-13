x,a,b=map(int,input().split())

A=abs(x-a)
B=abs(x-b)
if min(A,B) == A:
    print('A')
else:
    print('B')