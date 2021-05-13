def makeFibonacci(n):
    if n <= 1:
        return str(1)
    F = [None]*(n+1)
    F[0] = 1
    F[1] = 1
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i - 2]
    return str(F[n])

n = int(input())
print(makeFibonacci(n))