A,B,C=map(int,input().split())
x=max(A,B,C)
y=3*x-A-B-C
if y%2==0:
    print(y//2)
else:
    print((y+3)//2)
