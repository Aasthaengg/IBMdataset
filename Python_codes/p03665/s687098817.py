n, p = map(int, input().split())
la = [int(i) % 2 for i in input().split()]

n0 = sum(1 for a in la if a % 2 == 0)
n1 = sum(1 for a in la if a % 2 == 1)


def combi(n, k):
    c = 1
    for i in range(1, n + 1):
        c *= i
    for i in range(1, k + 1):
        c //= i
    for i in range(1, n - k + 1):
        c //= i
    return c


def answer():
    if p == 0:
        c0 = 2 ** n0
        c1 = 0
        for i in range(0, n1 + 1, 2):
            c1 += combi(n1, i)
        return c0 * c1
    else:
        c0 = 2 ** n0
        c1 = 0
        for i in range(1, n1 + 1, 2):
            c1 += combi(n1, i)
        return c0 * c1

print(answer())
