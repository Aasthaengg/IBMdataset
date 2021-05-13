N=raw_input()
N = [int(i) for i in N.split()]
m,n = (N[1],N[0]) if N[1] > N[0] else (N[0],N[1])
def gcd(m, n):
    if ((m % n) == 0):
        return n
    else:
        return gcd(n, m % n)
print gcd(m,n)