def main():
    n = int(input())
    a, b = n // 15, n % 15

    fbeg = [i for i in range(1, 16) if i % 3 != 0 and i % 5 != 0]
    fend = [i for i in range(a * 15, n + 1) if i % 3 != 0 and i % 5 != 0]

    ne = len(fbeg)
    fbs = sum(fbeg) # sum of first terms in [1, 15]
    fes = sum(fend)
    step = 15 * ne
    first = fbs
    last = fbs + (a-1) * step

    tot = (first + last) * a // 2 + fes

    print(tot)

main()
