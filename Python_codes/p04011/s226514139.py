#ABC044A
n=int(input())
k=int(input())
x=int(input())
y=int(input())
sum_=0
if n-k>0:
    sum_=k*x+(n-k)*y
else:
    sum_=n*x
print(sum_)