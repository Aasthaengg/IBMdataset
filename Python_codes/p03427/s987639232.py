n = int(input())
L = len(str(n))

def sumdigit(i):
    return sum(map(int, list(str(i))))

print(max([sumdigit(n - (n%(10**i) + 1)) for i in range(1, L)] + [sumdigit(n)]))
