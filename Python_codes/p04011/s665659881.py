n=int(input())
k=int(input())
x=int(input())
y=int(input())
if n>=k:
    a=k*x
    a+=(n-k)*y
else:
    a=n*x
print(a)