n=int(input())
k=int(input())
p1=int(input())
p2=int(input())
if n>k:
    print(k*p1+(n-k)*p2)
else:
    print(n*p1)