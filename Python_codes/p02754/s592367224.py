N,A,B=map(int,input().split())
s=0
a=N//(A+B)
s+=A*a
b=N-a*(A+B)
if b>=A:
    s+=A
else:
    s+=b
print(s)