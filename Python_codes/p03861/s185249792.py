a,b,x = map(int,input().split())

def f(n,x):
    return n//x

print(f(b,x)-f(a-1,x))