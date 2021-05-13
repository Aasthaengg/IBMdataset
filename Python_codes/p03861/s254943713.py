a,b,x = map(int,input().split())
def f(n):
    return n//x
print(f(b) - f(a-1))