a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
def g(x):
    if x%10==0:
        return 10
    else:
        return x%10
m=min(g(a),g(b),g(c),g(d),g(e))
def f(x):
    if x%10==0:
        return x
    else:
        return (x//10+1)*10
a=f(a)
b=f(b)
c=f(c)
d=f(d)
e=f(e)
print(a+b+c+d+e+m-10)
