import sys

def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    table.sort(reverse=True)
    return table

def resolve():
    lines = sys.stdin.readlines()
    n, k = tuple(map(int, lines[0].split(' ')))
    a = list(map(int, lines[1].split(' ')))
    divs = divisor(sum(a))

    for div in divs:
        a_mod = list(map(lambda x: x % div, a))
        sum_mod = sum(a_mod)
        a_mod.sort(reverse=True)
        loop = sum_mod//div
        for i in range(loop):
            a_mod[i] = 0
        sum_e_mod = sum(a_mod)
        if k >= sum_e_mod:
            print(div)
            return
    print(1)

resolve()