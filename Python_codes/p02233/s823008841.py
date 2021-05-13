n = int(input())
L = [-1]*(n+1)
def fib(i,L):
    if i <= 1:
        return 1
    else:
        if L[i] != -1:
            return L[i]
        else:
            L[i] = fib(i-1,L)+fib(i-2,L)
            return L[i]
        return fib(i-1,L)+fib(i-2,L)
print(fib(n,L))
