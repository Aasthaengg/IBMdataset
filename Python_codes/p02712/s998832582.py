n=int(input())

goukei=n*(n+1)*(1/2)
a=n//3
goukei-=3*(a)+3*a*(a-1)*(1/2)
b=n//5
goukei-=5*(b)+5*b*(b-1)*(1/2)
c=n//15
goukei+=15*(c)+15*c*(c-1)*(1/2)

print(int(goukei))