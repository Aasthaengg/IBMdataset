def f(a,b):
    if b:
        return f(b,a%b)
    return a
n=int(input())
a=list(map(int,input().split()))
p=f(a[0],a[1])
for i in a:
    p=f(p,i)
print(p)