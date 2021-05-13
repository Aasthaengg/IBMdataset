A,B=map(int,input().split())
a=max(A,B)
b=max(A,B,A-1,B-1)
c=a+b
if A==B:
    print(c)
else:
    print(c-1)