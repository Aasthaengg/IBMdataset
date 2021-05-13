a, b = map(int, input().split())

def factors_count(n):
    facs = dict()
    while n%2 == 0:
        facs.setdefault(2, 0)
        facs[2] += 1
        n //=2

    for f in range(3, int(n**0.5)+ 1, 2):
        while n%f == 0:
            facs.setdefault(f, 0)
            facs[f] += 1
            n //= f
    if n != 1:
        facs.setdefault(n, 0)
        facs[n] += 1
    return facs

afacs = factors_count(a)
bfacs = factors_count(b)

facs = set(afacs.keys()) & set(bfacs.keys())
print(len(facs)+1)
