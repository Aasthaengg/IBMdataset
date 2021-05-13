n=int(input())
k=int(input())
x=int(input())
y=int(input())

if(n>=k):
    sum = k*x+(n-k)*y
else:
    sum = x*n
print(sum)