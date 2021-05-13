import fractions

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

def main():
    N, M = map(int, input().split())
    S = input()
    T = input()

    L = lcm(N, M)
    ln = L//N
    lm = L//M
    n = {1+i*ln: s for i, s in enumerate(S)}
    m = {1+i*lm: t for i, t in enumerate(T)}
    
    for k in set(n.keys()).intersection(set(m.keys())):
        if n[k] != m[k]:
            return -1

    return L

print(main())