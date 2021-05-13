x,a,b = map(int,input().split())

A=x-a
B=x-b
if(A<0):
    A=-A
if(B<0):
    B=-B
if(A<B):
    print("A")
else:
    print("B")