x,k,d=map(int,input().split())
x=abs(x)
q=x//d
if (k-q < 0):
    print(x-d*k)
elif (k-q) % 2 == 0:
    print(x-d*q)
else:
    print(d*(1+q)-x)