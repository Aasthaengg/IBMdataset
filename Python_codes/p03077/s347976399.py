n=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
def f(x,y):
    return int((x+y-1)/y)

if e<d:
    d=e
if d<c:
    c=d
if c<b:
    b=c
if b<a:
    a=b
print(f(n,a)+4)
    
