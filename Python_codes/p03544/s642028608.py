n = int(input())
L = [0] * (n+1)
L[0] = 2
L[1] = 1

def lucas(n):
    if L[n] > 0:
        return L[n]
    L[n] = lucas(n-1) + lucas(n-2)
    return L[n]

print(lucas(n))
