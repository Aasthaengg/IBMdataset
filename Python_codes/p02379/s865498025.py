a,b,c,d=map(float,input().split())

k=c-a
l=d-b

n=(k*k+l*l)**(1/2)

print('{:.8f}'.format(n))
