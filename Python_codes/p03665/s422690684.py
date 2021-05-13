# AGC017A

def f(n, p, a):
    odd = sum(i % 2 for i in a)
    if odd == 0:
        if p == 0:
            return 2**n
        elif p == 1:
            return 0
    else:
        return 2**(n-1)
        
n, p = map(int, input().split())
a = list(map(int, input().split()))
print(f(n, p, a))
