n=int(input())
def Fib(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return b
print(Fib(n))
