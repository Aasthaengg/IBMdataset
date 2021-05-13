def fib(n):
    global f
    if f[n]==False:
        val=fib(n-1)+fib(n-2)
        f[n]=val
        return val
    else:
        return f[n]


n=int(input())
N=44+1
f=[1,1]
f.extend([0]*N)
fib(N)
print(f[n])