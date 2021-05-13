n=int(input())
a=n//3
b=n//5
c=n//15

print(n*(n+1)//2-3*a*(a+1)//2-5*b*(b+1)//2+15*c*(c+1)//2)
