
a,b,n=[int(x) for x in input().split()]
x=min((b-1),n)
f=(a*x)//b-(a*(x//b))
print(f)