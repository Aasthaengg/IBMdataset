A,B=map(int,input().split())
a=0
if B%A==0:
    a=A+B
else:
    a=B-A
print(a)