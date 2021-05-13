n=int(input())
k=int(input())
x,y=int(input()),int(input())
if(n<k):
    print(n*x)
else:
    print(x*k+(n-k)*y)
