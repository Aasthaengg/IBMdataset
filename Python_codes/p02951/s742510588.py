A,B,C=map(int,input().split())
a=A-B
b=C-a
if b<=0:
    print(0)
else:
    print(b)