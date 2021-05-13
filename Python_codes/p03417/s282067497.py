def c(n):
    if n == 1:
        return n
    elif n == 2:
        return 0
    else:
        return n-2

N,M = map(int,input().split())
print(c(N)*c(M))