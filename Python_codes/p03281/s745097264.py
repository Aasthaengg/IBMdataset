from math import ceil
def numdiv(n):
    c=0
    k=int((n)**0.5)
    for i in range(1,k+1):
        if n%i==0:
            c+=2
    if k==ceil(n**0.5):
        return c-1
    return c

c=0
n=int(input())
for i in range(3,n+1,2):
    if numdiv(i)==8:
        c+=1


print(c)